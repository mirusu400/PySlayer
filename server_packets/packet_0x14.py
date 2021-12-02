from lib import CSNSocket
from lib import p8, p16, p32, p64, p8u, p16u, p32u, p64u, pf32, pf64, pstr

import random

# Supermode Packet
def opcode_14():

    payload = b"\x14"  # opcode 0x14
    payload += p8u(1)  # Bool, 1
    return payload