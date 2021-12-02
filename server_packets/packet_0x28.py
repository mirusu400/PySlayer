from lib import CSNSocket
from lib import p8, p16, p32, p64, p8u, p16u, p32u, p64u, pf32, pf64, pstr

import random

# SetHp
def opcode_28(idx: int):

    payload = b"\x28"  # opcode 0x28
    payload += p16u(idx & 0xFFFF)  # Item
    return payload