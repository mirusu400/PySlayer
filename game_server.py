import socket
import time
import random
from _thread import *
from threading import Thread
from lib import CSNSocket
from lib import DBHelper
from lib import up32u
from server_packets import *
from client_packets import *
from plugin.player import Player
from plugin.custom_cmd import Custom_CMD
from plugin.binprint import BinPrint
from plugin.maps import Maps
from plugin.ip_connector import Ip_Connector
from typing import List, Optional

m = Maps()
i = Ip_Connector()


class Game_Tcp_Handler:
    # Every one player for one class
    def __init__(self, conn: socket.socket, addr: tuple):
        self.conn = conn
        self.addr = addr
        self.csn_socket = CSNSocket()
        self.db_helper = DBHelper()

        self.is_listening = True
        self.send_start_packet = False
        print("[+] New connection from", addr[0])
        self.index = i.get_index_from_ip(addr[0])

        cinfo = self.db_helper.get_characters(self.index)
        apparences = self.db_helper.get_apparence(self.index)
        equips = self.db_helper.get_equips(self.index)

        self.player = Player(cinfo, apparences, equips)
        self.custom_cmd = Custom_CMD(self.player, self)

        self.conn.sendall(self.csn_socket.build(self.player.get_welcome_packet()))

    def __str__(self):
        return f"{self.addr} \t {self.get_ip()} \t {self.player.character_name}"

    def get_ip(self):
        return self.player.ip

    def handle_client(self):
        while True:
            if self.is_listening == False:
                break
            data = self.conn.recv(1024)
            size = 0
            pos = 0
            if data == b"":
                break
            while True:
                size = data[pos]
                self.process_packet(data[pos : pos + size])
                pos += size
                if pos >= len(data):
                    break
        print("[-] Connection closed")
        self.is_listening = False
        self.conn.close()
        return

    def stop(self):
        self.is_listening = False

    def process_packet(self, data):
        if not data or data == b"":
            return -1
        csn = self.csn_socket
        csn.decrypt(data)

        if csn.recv_opcode != 0xD:

            csn.printheader()
            b = BinPrint(csn.recv_decrypt_payload)
            b.print()

        opcode = csn.recv_opcode
        # MoveandSaveCharacter
        if opcode == 0xD:  
            parse_0D(csn.recv_decrypt_payload)
            # csn.printdata()
            pass
            # print(f"[+] MoveandSaveCharacter: {xpos}, {ypos}")

        # User chatting
        elif opcode == 0x3:

            length, text = parse_03(csn.recv_decrypt_payload)
            print(f"[+] User chatting: {text}")
            if text[0] == "/":
                # Process Command
                payload = self.custom_cmd.get_chatting_cmd(text[1:])
                self.conn.sendall(self.csn_socket.build(payload))
            else:
                # Normal Chatting; broadcast to map
                payload = opcode_16(self.player.get_username(), text)
                broadcast_to_map(self.player.current_map, payload)
        
        # Addin stats
        elif opcode == 0x4:
            payload = self.player.add_stats(int(csn.recv_decrypt_payload[1]))
            self.conn.sendall(self.csn_socket.build(payload))
        
        # TODO: Create new User
        elif opcode == 0xE:
            parse_0E(csn.recv_decrypt_payload)
            payload = opcode_1C()
            self.conn.sendall(self.csn_socket.build(payload))

        # ConsumeItemOrSkill
        elif opcode == 0x15:
            item = parse_15(csn.recv_decrypt_payload)
            item_info = self.db_helper.get_item_info(item)
            print(f"[+] UseItemorSkill: {item}, {item_info['name']}")
            # 소비 아이템
            if item_info["Type"] == 0:
                # TODO: 귀환석 추가
                payload = self.player.set_delta_hp(item_info["HP"])
                self.conn.sendall(self.csn_socket.build(payload))
                payload = self.player.set_delta_mp(item_info["MP"])
                self.conn.sendall(self.csn_socket.build(payload))
                payload = [opcode_25(300), opcode_19(item, 1)]
                self.conn.sendall(self.csn_socket.build(payload))
            # 장비 아이템
            elif item_info["Type"] == 1:
                pass
            # 기타 아이템
            elif item_info["Type"] == 2:
                pass
            # 스킬
            elif item_info["Type"] == 3:
                if item_info["Con"] > 0:
                    time = item_info["Con"]
                    payload = self.player.get_usebuffskill_packet(item, time)
                    self.conn.sendall(self.csn_socket.build(payload))
                payload = self.player.set_delta_hp(item_info["HP"])
                self.conn.sendall(self.csn_socket.build(payload))
                payload = self.player.set_delta_mp(item_info["MP"])
                self.conn.sendall(self.csn_socket.build(payload))

        elif opcode == 0x16:  # AcceptQuest
            pass
        elif opcode == 0x2B:  # EnterGame (2B)
            if self.send_start_packet == False:

                self.player.ip = parse_2B(csn.recv_decrypt_payload)
                print(f"[+] EnterGame: {self.player.ip}")
                m.add_tcp_conntion_to_maps(self)
                broadcast_to_map(self.player.current_map, opcode_05(self), [self])

                payload = self.player.get_ingame_packet()
                self.conn.sendall(csn.build(payload))

                payload = self.player.get_spawn_packet(self)
                self.conn.sendall(csn.build(payload))

                # Send welcome chat
                payload = opcode_0A("Welcome to Pyslayer!", "mirusu400")
                self.conn.sendall(csn.build(payload))

                self.send_start_packet = True

        # BuyItemOrSckill
        elif opcode == 0x0B:  
            item, count = parse_0B(csn.recv_decrypt_payload)
            item_info = self.db_helper.get_item_info(item)

            if item_info["Type"] == 3:  # Skill
                self.player.add_skill(item)

            payload = opcode_18(item, count)
            self.conn.sendall(csn.build(payload))
        # elif opcode == 0x38:
        #     payload_list = []
        #     payload_list.append(opcode_20(6, 1))
        #     payload_list.append(opcode_20(8, 2))
        #     payload_list.append(opcode_20(9, 3))
        #     payload_list.append(opcode_20(0xA, 4))
        #     payload_list.append(opcode_20(0xB, 5))
        #     self.conn.sendall(csn.build(payload_list))
        elif opcode == 0x39:
            fight_type = parse_39(csn.recv_decrypt_payload)
            payload = opcode_20(fight_type, 12 if fight_type < 0xA else 8)
            self.conn.sendall(csn.build(payload))

        # SellItem
        elif opcode == 0x0C:  
            item, count = parse_0C(csn.recv_decrypt_payload)
            payload = opcode_19(item, count)
            self.conn.sendall(csn.build(payload))

        # GetListOfRooms
        elif opcode == 0x2C:
            code = parse_2C(csn.recv_decrypt_payload)
            if code == 0x01:
                payload = opcode_33()
                self.conn.sendall(csn.build(payload))
            elif code == 0x04:
                payload = opcode_A1()
                self.conn.sendall(csn.build(payload))
            else:
                print(f"[-] GetListOfRooms: Unknown code {code}")
        
        # TODO: Equip Item
        elif opcode == 0x1A:
            unk1, unk2 = parse_1A(csn.recv_decrypt_payload)
            # payload = opcode_34()
            # self.conn.sendall(csn.build(payload))

        # ChangeMap
        elif opcode == 0x7E:
            
            map_file_code, xpos, ypos = parse_7E(
                csn.recv_decrypt_payload, self.player.current_map, self.db_helper
            )

            m.change_map(self, self.player.current_map, map_file_code)

            print(m._maps)

            self.player.set_current_map(map_file_code, xpos, ypos)

            print(
                f"[*] Current map: {self.player.current_map}\t Portal_code: {up32u(csn.recv_decrypt_payload[1:5])}\t"
            )
            payload = self.player.get_changemap_packet()
            self.conn.sendall(csn.build(payload))

            payload = self.player.get_spawn_packet(self)
            self.conn.sendall(csn.build(payload))
        else:
            print("[-] Wrong Packet")


class Game_Server(Thread):
    def __init__(self, lock, tcp_port=7012):
        """
        Create a new tcp server
        """
        Thread.__init__(self)
        self.lock = lock
        self.tcp_port = int(tcp_port)
        self.is_listening = True
        self.sock = None
        self.msg = '{"success": "%(success)s", "message":"%(message)s"}'
        self.conn = None
        self.send_start_packet = False
        self.custom_cmd = Custom_CMD()
        self.client_list = []

    def run(self):
        """
        Start tcp server
        """
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind(("0.0.0.0", self.tcp_port))
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
            print(
                f"[+] Game Server Ch1. {time_reference}: {addr} {conn} connected at idx {len(self.client_list) + 1}."
            )
            tcpsocket = Game_Tcp_Handler(conn, addr)
            if self.custom_cmd.connection == None:
                self.custom_cmd.set_connection(tcpsocket)
            self.client_list.append(tcpsocket)

            start_new_thread(tcpsocket.handle_client, ())
            for idx, item in enumerate(self.client_list):
                if item.is_listening == False:
                    del self.client_list[idx]
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
        self.custom_cmd.set_player(self.client_list[0].player)
        payload = self.custom_cmd.get_custom_cmd_packet(data)
        print(payload)
        if payload != None:
            self.client_list[0].conn.sendall(
                self.client_list[0].csn_socket.build(payload)
            )

    def stop(self):
        """
        Stop tcp data
        """
        self.sock.close()
        self.is_alive = False


def broadcast_to_map(map_id, packet, exclude: Optional[List[Game_Tcp_Handler]] = None):
    for connection in m.get_tcp_connections_in_map(map_id):
        if exclude is not None and connection in exclude:
            continue
        print(
            f"send packet to {connection.player.character_name} ({connection.player.uid})"
        )
        connection.conn.sendall(connection.csn_socket.build(packet))
    return
