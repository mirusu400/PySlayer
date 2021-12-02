from lib import CSNSocket
from lib import p8, p16, p32, p64, p8u, p16u, p32u, p64u, pf32, pf64, pstr

import random

# GetItem/skill
def opcode_19(idx: int, count: int):

    # 64 16 16
    # while(8) { 16 }
    # 16
    payload = b"\x19"  # opcode 0x19
    payload += p64u(999999)  # Gold
    payload += p16u(idx)  # idx
    payload += p16u(count)  # Item
    payload += p8(0)  # ??
    for i in range(0):
        payload += p16u(random.randint(1, 10000))
    payload += p16(0)  # ??
    return payload