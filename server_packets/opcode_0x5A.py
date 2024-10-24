from lib import CSNSocket
from lib import p8, p16, p32, p64, p8u, p16u, p32u, p64u, pf32, pf64, pstr

import random


# Unknown, but it sends packet for something
def opcode_5A(unk: int):
    payload = b"\x5A"
    payload += p32(unk)
    return payload
