from lib import CSNSocket
from lib import p8, p16, p32, p64, p8u, p16u, p32u, p64u, pf32, pf64, pstr

import random

# About Cash??
def opcode_80():

    payload = b"\x80"
    payload += p8(1)
    payload += p32u(0x4CF)
    return payload