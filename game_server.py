import socket
import time
import random
from _thread import *
from threading import Thread
from lib import CSNSocket
from lib import up32u
from server_packets import *
from client_packets import *
class Game_Tcp_Handler():
    def __init__(self, conn, addr, db_conn):
        self.conn = conn
        self.addr = addr
        self.csn_socket = CSNSocket()
        self.db_conn = db_conn
        self.db_cur = self.db_conn.cursor()
        self.is_listening = True
        self.send_start_packet = False
        self.current_user_map = 401
        self.conn.sendall(self.csn_socket.build(opcode_02()))

    def handle_client(self):
        while True:
            if self.is_listening == False:
                break
            data = self.conn.recv(1024)
            if data == b'':
                print(f"[-] Connection closed")
                break
            size = 0
            pos = 0
            while True:
                size = data[pos]
                self.process_packet(data[pos:pos+size])
                pos += size
                if pos >= len(data):
                    break
        self.conn.close()
        return
    
    def stop(self):
        self.is_listening = False
        

    def process_packet(self, data):
        if not data or data == b'':
            return -1
        csn = self.csn_socket

        csn.decrypt(data)
        if csn.recv_opcode != 0xD:
            csn.printheader()
            csn.printdata()
        opcode = csn.recv_opcode
        if opcode == 0xD: # MoveandSaveCharacter
            # xpos, ypos = parse_0D(csn.recv_decrypt_payload)
            # csn.printdata()
            pass
            # print(f"[+] MoveandSaveCharacter: {xpos}, {ypos}")
        elif opcode == 14:  # CreateCharacter
            pass
        elif opcode == 22:  # AcceptQuest
            pass
        elif opcode == 43:  # EnterGame
            if self.send_start_packet == False:
                self.db_cur.execute('SELECT * FROM characters WHERE "index"=1')
                rows = self.db_cur.fetchall()[0]
                self.db_cur.execute('SELECT * FROM chracterequip WHERE "index"=1')
                equips = self.db_cur.fetchall()[0]
                self.db_cur.execute('SELECT * FROM chracterapparence WHERE "index"=1')
                apparences = self.db_cur.fetchall()[0]
                print(rows)
                (index, username, charactername, mapcode, job1, job2, _str, _dex, _int, _guts, _xpos, _ypos, level, hp, mp) = rows
                
                
                payload = opcode_03(mapcode)
                self.conn.sendall(csn.build(payload))

                payload = opcode_07(rows, equips, apparences)
                self.conn.sendall(csn.build(payload))
            
                
                for i in [80, 82, 86, 88, 90, 94, 0x15B]:
                    payload = opcode_18(i, 1)
                    self.conn.sendall(csn.build(payload))
                # for i in range(80, 0xFFFF):
                    # csn = opcode_18(i, 1)
                    # self.conn.sendall(csn.build())
                self.send_start_packet = True
        elif opcode == 0x0B:  # GetItemOrSkill
            item, count = parse_0B(csn.recv_decrypt_payload)
            payload = opcode_18(item, count)
            self.conn.sendall(csn.build(payload))
        
        elif opcode == 0x0C:  # SellItem
            item, count = parse_0C(csn.recv_decrypt_payload)
            payload = opcode_19(item, count)
            self.conn.sendall(csn.build(payload))

        elif opcode == 126: # ChangeMap
            # csn = opcode_03(401)
            map_file_code, xpos, ypos = parse_7E(csn.recv_decrypt_payload, self.current_user_map, self.db_cur)
            print(f"[*] Current map: {self.current_user_map}\t Portal_code: {up32u(csn.recv_decrypt_payload[1:5])}\t")
            self.current_user_map = map_file_code
            self.db_cur.execute('SELECT * FROM characters WHERE "index"=1')
            rows = self.db_cur.fetchall()[0]
            self.db_cur.execute('SELECT * FROM chracterequip WHERE "index"=1')
            equips = self.db_cur.fetchall()[0]
            self.db_cur.execute('SELECT * FROM chracterapparence WHERE "index"=1')
            apparences = self.db_cur.fetchall()[0]

            payload = opcode_08(self.current_user_map)
            self.conn.sendall(csn.build(payload))

            # payload = opcode_05(xpos, ypos, 0x101)
            # self.conn.sendall(csn.build(payload))

            payload = opcode_07(rows, equips, apparences, xpos, ypos)
            self.conn.sendall(csn.build(payload))

            for i in [80, 82, 84, 86, 88, 90, 94, 0x15B]:
                payload = opcode_18(i, 1)
                self.conn.sendall(csn.build(payload))
        else:
            print("[-] Wrong Packet")


class Game_Server(Thread):
    def __init__(self, lock, db_conn, tcp_port=7012):
        """
        Create a new tcp server
        """
        Thread.__init__(self)
        self.lock = lock
        self.db_conn = db_conn
        self.db_cur = self.db_conn.cursor()
        self.tcp_port = int(tcp_port)
        self.is_listening = True
        self.sock = None
        self.msg = '{"success": "%(success)s", "message":"%(message)s"}'
        self.conn = None
        self.send_start_packet = False
        self.client_list = []

    def run(self):
        """
        Start tcp server
        """
        self.sock = socket.socket(socket.AF_INET,
                                  socket.SOCK_STREAM)
        self.sock.bind(('127.0.0.1', self.tcp_port))
        self.sock.setblocking(0)
        self.sock.settimeout(1)
        time_reference = time.time()
        self.sock.listen(1)

        while self.is_listening:
            conn, addr = None, None
            try:
                conn, addr = self.sock.accept()
            except socket.timeout:
                continue
            time_reference = time.time()
            print(f"[+] Game Server Ch1. {time_reference}: {addr} connected at idx {len(self.client_list) + 1}.")
            tcpsocket = Game_Tcp_Handler(conn, addr, self.db_conn)
            self.client_list.append(tcpsocket)
            
            start_new_thread(tcpsocket.handle_client, ())
            # TODO: remove client from list when disconnected
        for client in self.client_list:
            try:
                client.stop()
            except:
                continue
            
        self.stop()
        print("[-] Game Server Closed")

    def send_custom_opcode(self, data):
        """
        Send custom opcode
        """
        payload = None
        if data == "13":
            payload = opcode_13()
        elif data == "18" or data == "item":
            item = int(input("item code?"))
            count = int(input("count?"))
            payload = opcode_18(item, count)
        elif data == "map":
            map = int(input("map code?"))
            self.client_list[0].current_user_map = map
            self.db_cur.execute('SELECT * FROM characters WHERE "index"=1')
            rows = self.db_cur.fetchall()[0]
            self.db_cur.execute('SELECT * FROM chracterequip WHERE "index"=1')
            equips = self.db_cur.fetchall()[0]
            self.db_cur.execute('SELECT * FROM chracterapparence WHERE "index"=1')
            apparences = self.db_cur.fetchall()[0]
            
            payload = opcode_08(map)
            self.client_list[0].conn.sendall(self.client_list[0].csn_socket.build(payload))

            payload = opcode_07(rows, equips, apparences)
            self.client_list[0].conn.sendall(self.client_list[0].csn_socket.build(payload))
            for i in [80, 82, 86, 88, 90, 94, 0x15B]:
                payload = opcode_18(i, 1)
                self.client_list[0].conn.sendall(self.client_list[0].csn_socket.build(payload))
            return

        elif data == "28":
            item = int(input("code?"))
            payload = opcode_28(item)
        elif data == "29":
            payload = opcode_29()
        elif data == "51":
            item = int(input("code?"))
            payload = opcode_51(item)
        elif data == "80":
            payload = opcode_80()
        elif data == "D7":
            item = int(input("code?"))
            payload = opcode_D7(item)
        elif data == "AE":
            item = int(input("code?"))
            payload = opcode_AE(item)
        elif data == "superman":
            payload = opcode_99(0x13)
        elif data == "supermode":
            payload = opcode_99(0x14)
        elif data == "mob":
            # item = int(input("mob code?"))
            for i in range(0, 0xFFFF):
                payload = opcode_25(i,i,i)
                self.client_list[0].conn.sendall(self.client_list[0].csn_socket.build(payload))
                time.sleep(0.1)
            return
            # payload = opcode_25(item)
        else:
            print("[-] Undefined Opcode")
            return
        self.client_list[0].conn.sendall(self.client_list[0].csn_socket.build(payload))
        

    def stop(self):
        """
        Stop tcp data
        """
        self.sock.close()
        self.is_alive = False
