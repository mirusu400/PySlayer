from lib import CSNSocket
from lib import p8, p16, p32, p64, p8u, p16u, p32u, p64u, pf32, pf64, pstr
import socket

host_ip_table = list(map(int, socket.gethostbyname(socket.gethostname()).split(".")))


def opcode_01():
    payload = b"\x01"
    # Maybe game version
    # Yahoo! ver. WS: 317
    payload += p16(0x13D)

    # Size of string packet
    payload += p16(60)
    payload += pstr("Unofficial Server Emulator, Pyslayer By. mirusu400", 60)
    payload += p8(2)  # worldCount

    payload += p8(2)
    payload += p8(2)
    payload += p8(2)
    payload += p8(1)

    payload += p16(1)
    payload += p8u(host_ip_table[3])
    payload += p8u(host_ip_table[2])
    payload += p8u(host_ip_table[1])
    payload += p8u(host_ip_table[0])
    payload += p32(7012)
    payload += p8(0)

    payload += p16(1)

    # This is for Test server
    payload += p8u(59)
    payload += p8u(1)
    payload += p8u(168)
    payload += p8u(192)
    payload += p32(7012)
    payload += p8(0)
    return payload
