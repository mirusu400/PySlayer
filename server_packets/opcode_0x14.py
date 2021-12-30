from lib import CSNSocket
from lib import p8, p16, p32, p64, p8u, p16u, p32u, p64u, pf32, pf64, pstr

import random

# UpdateStats Packet
def opcode_14(type, value):
    payload = b"\x14"  # opcode 0x14
    # p32 p8 p16
    payload += p32u(2)  # Character UID
    payload += p8u(type)
    payload += p16u(value)  # Bool, 1
    return payload