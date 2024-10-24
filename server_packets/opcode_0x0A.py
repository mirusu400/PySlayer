from lib import CSNSocket
from lib import p8, p16, p32, p64, p8u, p16u, p32u, p64u, pf32, pf64, pstr

import random


# Whisper
def opcode_0A(chat, username, channel=101):
    payload = b"\x0A"  # opcode 0x0A
    # Maybe sender's channel? I don't know
    # If 101, same channel (<From: %s> %s)
    # Else, different channel (<From: %s[%s-%u]> %s)
    payload += p8u(channel)
    # Sender
    payload += pstr(username, 17)
    # Chat size
    payload += p8u(len(chat))
    # Chat message
    payload += pstr(chat, len(chat))
    return payload
