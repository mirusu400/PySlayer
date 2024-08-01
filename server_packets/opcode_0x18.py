from lib import CSNSocket
from lib import p8, p16, p32, p64, p8u, p16u, p32u, p64u, pf32, pf64, pstr

import random


# GetItem/skill
def opcode_18(idx: int, count: int) -> bytes:
    # csn = CSNSocket()
    payload = b"\x18"  # opcode 0x14
    payload += p64u(999999)  # Gold
    payload += p32u(999999)  # Winnie
    payload += p16u(idx)  # Item
    payload += p16(count)  # Count?
    return payload
