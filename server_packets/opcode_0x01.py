from lib import CSNSocket
from lib import p8, p16, p32, p64, p8u, p16u, p32u, p64u, pf32, pf64, pstr
import socket
hostiptable = list(map(int, socket.gethostbyname(socket.gethostname()).split(".")))


def opcode_01():
    payload = b"\x01"
    payload += p16(0x13D)
    payload += p16(60)
    payload += pstr("Unofficial Server Emulator, Pyslayer By. mirusu400", 60)
    payload += p8(2) #worldCount

    payload += p8(2)
    payload += p8(2)
    payload += p8(2)
    payload += p8(1)

    payload += p16(1)
    payload += p8u(hostiptable[3])
    payload += p8u(hostiptable[2])
    payload += p8u(hostiptable[1])
    payload += p8u(hostiptable[0])
    payload += p32(7012)
    payload += p8(0)

    payload += p16(1)
    payload += p8u(59)
    payload += p8u(1)
    payload += p8u(168)
    payload += p8u(192)
    payload += p32(7012)
    payload += p8(0)
    return payload