import socket
import time
import random
from server_packets.packet_0x02 import opcode_02

from threading import Thread
from lib import CSNSocket
from server_packets import *


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
        self.is_alive = False
        self.send_start_packet = False

    def run(self):
        """
        Start tcp server
        """
        self.sock = socket.socket(socket.AF_INET,
                                  socket.SOCK_STREAM)
        self.sock.bind(('127.0.0.1', self.tcp_port))
        self.sock.setblocking(0)
        self.sock.settimeout(5)
        time_reference = time.time()
        self.sock.listen(1)
        self.is_alive = True

        while self.is_listening:
            try:
                self.conn, addr = self.sock.accept()
            except socket.timeout:
                continue
            time_reference = time.time()
            print(f"[+] Game Server Ch1. {time_reference}: {addr} connected.")
            self.conn.sendall(opcode_02().build())
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
        self.stop()
        self.is_alive = False

    def process_packet(self, data):
        if not data or data == b'':
            return -1
        csn = CSNSocket()
        csn.decrypt(data)
        csn.printheader()
        csn.printdata()
        opcode = csn.recv_opcode
        if opcode == 14:  # CreateCharacter
            pass
        elif opcode == 22:  # AcceptQuest
            pass
        elif opcode == 43:  # EnterGame
            if self.send_start_packet == False:
                csn = opcode_03()
                self.conn.sendall(csn.build())

                csn = opcode_07()
                self.conn.sendall(csn.build())
                self.send_start_packet = True
        else:
            print("[-] Wrong Packet")

    def stop(self):
        """
        Stop tcp data
        """
        self.sock.close()
        self.is_alive = False
