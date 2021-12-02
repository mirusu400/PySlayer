from lib import CSNSocket
from lib import p8, p16, p32, p64, p8u, p16u, p32u, p64u, pf32, pf64, pstr

import random

# ??
def opcode_29():

    payload = b"\x29"  # opcode 0x28
    r1 = random.randint(0, 0xFFFFFFFF)
    r2 = random.randint(0, 0xFFFFFFFF)
    r3 = random.randint(0, 0xFFFFFFFF)
    print(r1, r2, r3)
    payload += p32u(random.randint(0, r1))  # ??
    payload += p32u(random.randint(0, r2))  # ??
    payload += p32u(random.randint(0, r3))  # ??
    
    return payload