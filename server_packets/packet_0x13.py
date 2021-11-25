from lib import CSNSocket
from lib import p8, p16, p32, p64, p8u, p16u, p32u, p64u, pf32, pf64, pstr

import random

# Superman Packet
def opcode_13():
    csn = CSNSocket()
    payload = b"\x13"  # opcode 0x14
    payload += p8u(1)  # Bool, 1
    return csn.inject_payload(payload)