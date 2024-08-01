from lib import CSNSocket
from lib import p8, p16, p32, p64, p8u, p16u, p32u, p64u, pf32, pf64, pstr

import random


# ??
def opcode_99(case):

    payload = b"\x99"
    if case == 0x13:
        payload += p8u(0x13)
        payload += p8u(0x01)
    elif case == 0x14:
        payload += p8u(0x14)
        payload += p8u(0x01)
    return payload
