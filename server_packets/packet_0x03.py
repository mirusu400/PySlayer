from lib import CSNSocket
from lib import p8, p16, p32, p64, p8u, p16u, p32u, p64u, pf32, pf64, pstr

import random

def opcode_03(mapcode):
    csn = CSNSocket()
    payload = b"\x03"
    x = random.randint(65535, 210000000)
    y = random.randint(1, 255)
    payload += p8u(1)  # Must be >= 1
    payload += p16u(mapcode)  # Mapcode
    payload += p32u(x)

    payload += p64u(976431)  # gold
    payload += p32u(30000)
    payload += p32u(1324567)  # 명성점수
    payload += p32u(7974)  # winnie
    payload += p32u(5)  # 전장 승
    payload += p32u(6)  # 전장 패
    payload += p32u(7)  # 전장 KO
    payload += p32u(8)  # 전장 Down

    payload += p8u(0)  # Bool
    
    print(x, y)
    payload += p32u(x)  # var_x
    # for i in range(0, 17):  # size 17 str
        # payload += p8u(i+10)
    payload += pstr("미루나무", 17) # Mentor name
    payload += p8u(y)  # var_y
    payload += p8u(10)

    # 최대 진행가능 퀘스트 == 5?
    for i in range(0, 5):
        payload += p16u(10+i)  # quest?
    for i in range(0, 5):
        payload += p8u(10+i)

    payload += p8u(15)  # 장비칸 개수
    payload += p8u(30)  # 소비칸 개수
    payload += p8u(30)  # 기타칸 개수

    payload += p8u(15)  # End Quest?

    for i in range(0, 15): # End Quest Count
        payload += p16u(i) # Quest ID
        payload += p8u(1) # 퀘스트 완료횟수

    # Equipment
    payload += p8u(0)
    for i in range(0):
        payload += p16u(90+(i*2))
        payload += p8u(5)
        for j in range(5): #enchant
            payload += p16u(j+10)
        payload += p16u(i+10)

    payload += p8u(0)
    for i in range(0):
        payload += p16u(90+(i*2))
        payload += p16u(4)

    payload += p8u(0)  # Other item list
    for i in range(0):
        payload += p16u(90+(i*2))
        payload += p8u(10)

    # { 16 8 }

    # Originally p32
    # Event time
    payload += p32u(0)
    return csn.inject_payload(payload)