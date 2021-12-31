import socket
import json
import time
from threading import Thread, Lock
from lib import CSNSocket
from lib import p8, p16, p32, p64
from server_packets import *

class Patch_Server(Thread):
    def __init__(self, lock, tcp_port = 1234):
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
        self.sock.bind(('0.0.0.0', self.tcp_port))
        self.sock.setblocking(0)
        self.sock.settimeout(1)
        time_reference = time.time()
        self.sock.listen(1)

        while self.is_listening:
            try:
                conn, addr = self.sock.accept()
            except socket.timeout:
                continue
            csnsocket = CSNSocket()
            time_reference = time.time()
            print(f"Patch server {time_reference}: {addr} connected.")
            # print(conn.recv(1024))
            conn.close()
        print("[-] Patch server Closed")
        self.stop()

        
    def stop(self):
        """
        Stop tcp data
        """
        self.sock.close()