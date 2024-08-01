from lib import CSNSocket
from lib import p8, p16, p32, p64, p8u, p16u, p32u, p64u, pf32, pf64, pstr

import random


# 전장
def opcode_A5():

    payload = b"\xA5"
    payload += p16u(201)  # Mapcode
    payload += p32u(1212)  # ??
    return payload
