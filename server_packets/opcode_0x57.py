from lib import CSNSocket
from lib import p8, p16, p32, p64, p8u, p16u, p32u, p64u, pf32, pf64, pstr

import random


# About Item/skill
# Maybe Quest Reward?
# 8 32 16
def opcode_57(unk: int):
    payload = b"\x57"
    a = random.randint(0, 50)
    payload += p8(1)
    payload += p32u(0x1F78A43)
    payload += p16u(unk)
    return payload
