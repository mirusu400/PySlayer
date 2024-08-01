from lib import CSNSocket
from lib import p8, p16, p32, p64, p8u, p16u, p32u, p64u, pf32, pf64, pstr

import random


def opcode_42(idx: int):
    payload = b"\x42"  # opcode 0x42

    a = random.randint(0, 50)
    payload += p32u(0x1F78A43)
    payload += p32u(0x1F78A43)
    payload += p16u(idx)
    return payload
