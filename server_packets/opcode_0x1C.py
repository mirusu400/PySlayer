from lib import CSNSocket
from lib import p8, p16, p32, p64, p8u, p16u, p32u, p64u, pf32, pf64, pstr

import random


# Create User
def opcode_1C() -> bytes:
    # csn = CSNSocket()
    payload = b"\x1C"  # opcode 0x14
    payload += p8(1)
    return payload
