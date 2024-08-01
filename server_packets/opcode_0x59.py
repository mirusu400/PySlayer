from lib import CSNSocket
from lib import p8, p16, p32, p64, p8u, p16u, p32u, p64u, pf32, pf64, pstr

import random


# ??
# About Item/skill
def opcode_59(unk: int):

    payload = b"\x59"
    a = random.randint(0, 50)
    payload += p8(a)  # v47 - 1 < 5
    payload += p8u(unk)
    return payload
