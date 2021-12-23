from lib import CSNSocket
from lib import p8, p16, p32, p64, p8u, p16u, p32u, p64u, pf32, pf64, pstr

import random

# SetMp
def opcode_44(amount = 0xFF):
    payload = b"\x44" 
    payload += p16u(amount)
    return payload