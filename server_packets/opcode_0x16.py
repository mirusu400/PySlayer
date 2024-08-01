from lib import CSNSocket
from lib import p8, p16, p32, p64, p8u, p16u, p32u, p64u, pf32, pf64, pstr

import random


# Normal chatting packet
def opcode_16(username, chatting):

    payload = b"\x16"  # opcode 0x16
    length = chatting.encode("euc-kr").__len__()
    payload += pstr(username, 17)

    payload += p8u(length)
    payload += pstr(chatting, length)
    return payload
