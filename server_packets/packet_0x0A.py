from lib import CSNSocket
from lib import p8, p16, p32, p64, p8u, p16u, p32u, p64u, pf32, pf64, pstr

import random

# Whisper
def opcode_0A(chat, username):
    payload = b"\x0A"  # opcode 0x0A
    payload += p8u(1)
    payload += pstr(username, 17)
    payload += p8u(len(chat))
    payload += pstr(chat, len(chat))
    return payload