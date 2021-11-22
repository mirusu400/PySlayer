from .packlib import *
from _key import xorKey
import struct
import binascii


class CSNSocket:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"): 
            print("CSNsocket::__new__ is called")
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        cls = type(self)
        if not hasattr(cls, "_init"):
            print("CSNsocket::__init__ is called")

            # seqnum is just the order that packet is sent/receive.
            self.send_packet_length = 0
            self.send_seqnum = 0
            self.send_opcode = 0
            self.send_hash = 0
            self.send_payload = None

            self.recv_packet_length = 0
            self.recv_seqnum = 0
            self.recv_opcode = 0
            self.recv_hash = 0
            self.recv_payload = None
            self.recv_decrypt_payload = None
        cls._init = True

    def build(self):
        p = b""
        p += p32(self.send_packet_length)
        p += p32(self.send_hash)  # hash
        p += self.send_payload
        return p

    def inject_payload(self, payload):
        self.send_seqnum = (self.send_seqnum + 1) & 0xFF
        self.send_payload = payload
        self.send_packet_length = (
            ((len(payload) + 8) & 0x3FFF) | self.send_seqnum << 12)
        return self

    def printheader(self):
        try:
            print(f"[*] length: {self.recv_packet_length}\topcode: {self.recv_opcode}\thash: {self.recv_hash}\tseqnum: {self.recv_seqnum}\txorkey: {(xorKey[4 * ((self.recv_seqnum +0xF) & 0xFF)])}")
        except:
            pass
        return

    def printdata(self):
        print(f"[*] Raw packet: {binascii.hexlify(self.recv_payload)}")
        print(f"[*] Dec packet: {binascii.hexlify(self.recv_decrypt_payload)}")
        return

    def encrypt(self):
        # Actually, we don't need encrypt data to send client.
        # Just for legacy and documentation.
        self.send_hash = xorKey[self.send_opcode]
        for idx, byte in enumerate(self.send_payload):
            self.send_hash += byte & 0x5F
            # encpayload = chr((byte ^ xorKey[self.opcode + 0xF]) & 0xFF)
        self.send_hash += xorKey[self.send_opcode + 0x25] + self.send_opcode

    def decrypt(self, payload):
        # 0~0x08 Bytes is header
        self.recv_payload = payload
        self.recv_packet_length = self.recv_payload[0]
        # ex : 1B 58 01 ..
        # lg ==1B
        # sq ==== 5
        # op ======
        self.recv_seqnum = (up32u(self.recv_payload[0:4]) >> 12) & 0xFF
        self.recv_hash = up32u(self.recv_payload[4:8])
        self.recv_decrypt_payload = self.recv_payload[8:]

        # For decrypt payload faster, I use array.
        dec = []
        for i in range(0, len(self.recv_decrypt_payload)):
            dec.append(self.recv_decrypt_payload[i] ^ (
                xorKey[4 * ((self.recv_seqnum + 0xF) & 0xFF)]))

        self.recv_decrypt_payload = bytes(dec)
        self.recv_opcode = self.recv_decrypt_payload[0]
