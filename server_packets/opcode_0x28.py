from lib import CSNSocket
from lib import p8, p16, p32, p64, p8u, p16u, p32u, p64u, pf32, pf64, pstr

import random

# setHp
def opcode_28(amount: int):
    payload = b"\x28"  # opcode 0x28
    payload += p16u(amount & 0xFFFF)  # Item
    return payload