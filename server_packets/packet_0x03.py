from lib import CSNSocket
from lib import p8, p16, p32, p64, p8u, p16u, p32u, p64u, pf32, pf64, pstr

import random

def opcode_03(mapcode):
    csn = CSNSocket()
    payload = b"\x03"
    payload += p8u(1)  # Must be >= 1
    payload += p16u(mapcode)  # Mapcode
    payload += p32u(15)

    payload += p64u(976431)  # gold
    payload += p32u(30000)
    payload += p32u(1324567)  # 명성점수
    payload += p32u(7974)  # winnie
    payload += p32u(5)  # 전장 승
    payload += p32u(6)  # 전장 패
    payload += p32u(7)  # 전장 KO
    payload += p32u(8)  # 전장 Down

    payload += p8u(1)  # Bool
    x = random.randint(1, 65535)
    y = random.randint(1, 255)
    payload += p32u(x)  # var_x
    for i in range(0, 17):  # size 17 str
        payload += p8u(i+10)
    payload += p8u(y)  # var_y
    payload += p8u(13)

    for i in range(0, 5):
        payload += p16u(10+i)  # quest?
    for i in range(0, 5):
        payload += p8u(0)

    payload += p8u(99)  # 장비칸 개수
    payload += p8u(99)  # 장비칸 개수
    payload += p8u(99)  # 소비칸 개수

    payload += p8u(7)  # ??

    for i in range(0, 7):
        payload += p16u(i+11)
        payload += p8u(1)

    # Equipment
    payload += p8u(10)
    for i in range(10):
        payload += p16u(9)
        payload += p8u(2)
        for j in range(2):
            payload += p16u(0)
        payload += p16u(i+10)
    # {
    #   16
    #   8 : { 16 }
    #   16
    # }
    #
    # Consume
    payload += p8u(10)
    for i in range(10):
        payload += p16u(i+10)
        payload += p16u(4)
    # {
    #   16 16
    # }
    payload += p8u(10)  # Other item list
    for i in range(10):
        payload += p16u(i)
        payload += p8u(10)
    # { 16 8 }

    # Originally p32
    # quests, items, etc..
    payload += p32u(0xFFFFFFFF)
    return csn.inject_payload(payload)