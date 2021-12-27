from lib import CSNSocket
from lib import p8, p16, p32, p64, p8u, p16u, p32u, p64u, pf32, pf64, pstr

import random

# Ingame Init packet
def opcode_04():

    payload = b"\x04"  # opcode 7
    v802 = 1
    payload += p8u(v802)  # Must be >= 1
    for i in range(v802):
        payload += pstr("미루나무", 17)
        payload += p32u(2)  # Must be 2
        payload += p32u(3000)
        payload += p16u(1)  # If 1, send packet below:

        payload += p8u(2)
        payload += pstr("나혼자산다", 17)

        # If >1, send packet below{str 16 16}:
        # If ==1, Bool
        # Guild info
        payload += p16u(0)
        # payload += pstr("MyGuild", 17)
        # payload += p16u(0)
        # payload += p16u(0)

        

        # if >= 4, send packet below:
        # {
        #   16 str
        #   if 4:
        #     16 16 16
        #   if else:
        #     16 16 16
        #   16
        # }
        payload += p8u(0)
        # payload += p16u(1)
        # payload += pstr("내혼녀", 17)
        # payload += p16u(10)
        # payload += p16u(11)
        # payload += p16u(12)
        # payload += p16u(13)

        # payload += p16u(1)
        # payload += b"mirusu403012345\0" #partnername

        # payload += p16u(0)
        # payload += p16u(0)
        # payload += p16u(0)
        # payload += p16u(0)

        # === end if
        # 4 == 도적 ( 2 == 트랩퍼)
        # 5 == 마법사
        # 6 == 사제
        payload += p8u(4) # 1차 전직
        payload += p8u(1) # 2차 전직
        # payload += p16u(12)
        payload += p8u(98)  # Level
        payload += p8u(20) # 계급

        payload += p8u(30)  # 성별?

        for i in range(0, 17):  # 외형
            payload += p16u(110+i)

        payload += p16u(999)  # 힘
        payload += p16u(999)  # 민첩
        payload += p16u(999)  # 지혜
        payload += p16u(999)  # 근성

        for i in range(0, 15):  # Equip
            payload += p16u(0x100)
            # payload += p16u(10)
            for j in range(0, 6): # Equip enchant
                payload += p16u(0)
        # line 1874

        for i in range(0, 10): # Cash Equip
            payload += p16(0)
            payload += p16(0)
            payload += p16(0)
            # payload += p16u(i+100)
            # payload += p16u(i+90)
            # payload += p16u(i+80)

        # line 1886
        payload += p8u(1)
        # lots of loop(64), but i dont knwo why
        # for i in range(0x40):
        for i in range(200):
            payload += p16u((i+10) % 0xDF) #Hp, Mp inside
            payload += p16u((i+10) % 0xDF) # Hp, Mp inside
        x = random.randint(1000,100000) / 100
        y = random.randint(100,1000) / 100
        # print(x, y)

        payload += p8u(0)

        payload += pf64(10000)
        payload += pf64(10000)

        payload += p32u(32)
        payload += p8u(1)  # Bool
        payload += p8u(0)

        payload += p32u(501)
        payload += p32u(502)
        payload += p8u(0)
        payload += p32u(503)

        payload += p8u(102)
        payload += p8u(101)
        payload += p8u(100)
        payload += p8u(99)

        payload += p8u(16)  # Bool
        payload += p8u(16)  # Bool
        payload += p8u(16)  # Bool
        payload += p8u(16)  # Bool
        payload += p8u(16)  # Bool
        payload += p8u(16)  # Bool
        payload += p8u(16)  # Bool

        payload += p16u(15)
        payload += p16u(16)

        payload += p32u(700)
        payload += p8u(30)

        # these packets are send on else method..
        payload += p8u(1) # bool
        payload += p8u(113)
        payload += pstr("123456789", 13)  # 13 bytes
        payload += p8u(12)
        payload += p8u(11)
        payload += p32u(800)
        payload += p8u(114)
        payload += p16u(11)
        payload += p16u(12)

        # for i in range(0,8000):
        #     payload += p8u(i % 0xFF)
    return payload