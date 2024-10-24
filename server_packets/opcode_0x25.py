from lib import CSNSocket
from lib import p8, p16, p32, p64, p8u, p16u, p32u, p64u, pf32, pf64, pstr

import random


# 개인상점? 아이템사용? 스킬사용?
def opcode_25(skill: int):

    payload = b"\x25"
    payload += p16u(skill)
    rand = 1

    # payload += p8u(1) # Bool
    # payload += p32u(x)
    # 52665, 5492
    # print(f"item:{item}, rand:{rand}, x:{x}, y:{y}")
    # print("item: " + str(item) + " qx: " + str(x) + " y: " + str(y))
    # if rand == 1:

    #     payload += p32u(x)
    # payload += p32u(y)
    # payload += p16(0x23)
    # payload += p16(0x24)

    return payload
