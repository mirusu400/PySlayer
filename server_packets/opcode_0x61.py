from lib import CSNSocket
from lib import p8, p16, p32, p64, p8u, p16u, p32u, p64u, pf32, pf64, pstr

import random


# About normal chat?
def opcode_61(idx=0):
    payload = b"\x61"  # opcode 0x61
    chat = "Hello world"
    payload += pstr("미루나무", 17)
    payload += p8(len(chat))
    payload += pstr(chat, len(chat))
    return payload
