from lib import CSNSocket
from lib import p8, p16, p32, p64, p8u, p16u, p32u, p64u, pf32, pf64, pstr

import random


# ??
def opcode_51(idx: int):

    payload = b"\x51"  # opcode 0x51
    payload += p16u(idx & 0xFFFF)  # Item
    return payload
