from lib import CSNSocket
from lib import p8, p16, p32, p64, p8u, p16u, p32u, p64u, pf32, pf64, pstr

import random


def opcode_2F():
    csn = CSNSocket()
    payload = b"\x2F"
    payload += p8u(201)
    payload += p8u(201)
    payload += p16u(201)
    payload += pstr("test",16)
    
    payload += p16u(201)  # Mapcode
    
    for i in range(9):
        payload += p8u(1)
    return csn.inject_payload(payload)