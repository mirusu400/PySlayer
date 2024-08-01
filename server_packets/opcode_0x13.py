from lib import CSNSocket
from lib import p8, p16, p32, p64, p8u, p16u, p32u, p64u, pf32, pf64, pstr

import random


# Create a new character
def opcode_13():

    payload = b"\x13"  # opcode 0x13
    payload += p8u(1)
    return payload
