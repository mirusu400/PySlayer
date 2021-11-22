import socket
import json
import time
from threading import Thread, Lock
from lib import CSNSocket
from lib import p8, p16, p32, p64
from server_packets import *

class Channel_Server(Thread):
    def __init__(self, lock, tcp_port = 7011):
        """
        Create a new tcp server
        """
        Thread.__init__(self)
        self.lock = lock
        self.tcp_port = int(tcp_port)
        self.is_listening = True
        self.msg = '{"success": "%(success)s", "message":"%(message)s"}'

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

        while self.is_listening:
            try:
                conn, addr = self.sock.accept()
            except socket.timeout:
                continue
            time_reference = time.time()
            print(f"Channel server {time_reference}: {addr} connected.")
            csn = opcode_01()
            conn.sendall(csn.build())
            conn.close()

        self.stop()

        
    def stop(self):
        """
        Stop tcp data
        """
        self.sock.close()