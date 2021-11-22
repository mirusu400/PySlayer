from lib import CSNSocket
from lib import p8, p16, p32, p64, p8u, p16u, p32u, p64u, pf32, pf64, pstr

import random

def opcode_07():
    csn = CSNSocket()
    payload = b"\x07"  # opcode 7
    payload += p8u(1)  # Must be >= 1
    payload += pstr("mirusu400", 17)
    payload += p32u(2)  # Must be 2
    payload += p32u(3000)
    payload += p16u(1)  # If 1, send packet below:

    payload += p8u(4)
    payload += pstr("Whatsthis", 17)

    # If >1, send packet below{str 16 16}:
    # If ==1, Bool
    # Guild info
    payload += p16u(2)
    payload += pstr("MyGuild", 17)
    payload += p16u(4)
    payload += p16u(5)

    payload += p8u(0)
    # if >= 4, send packet below:
    # {
    #   16 str
    #   if 4:
    #     16 16 16
    #   if else:
    #     16 16 16
    #   16
    # }

    # payload += p16u(1)
    # payload += b"mirusu403012345\0" #partnername

    # payload += p16u(0)
    # payload += p16u(0)
    # payload += p16u(0)
    # payload += p16u(0)

    # === end if

    payload += p8u(33)
    payload += p8u(34)
    payload += p8u(35)
    payload += p8u(98)  # Level

    payload += p8u(1)  # Bool

    for i in range(0, 17):  # 장비
        payload += p16u(112+i)

    payload += p16u(25)  # 힘
    payload += p16u(26)  # 민첩
    payload += p16u(27)  # 지혜
    payload += p16u(28)  # 근성

    for i in range(0, 15):  # Skills?
        payload += p16u(112+i)

        for j in range(0, 6):
            payload += p16u(j*10+i)
    # line 1874

    for i in range(0, 10):
        payload += p16u(1)
        payload += p16u(2)
        payload += p16u(3)

    # line 1886
    payload += p8u(1)
    # lots of loop(64), but i dont knwo why
    # for i in range(0x40):
    for i in range(200):
        payload += p16u((i*15) & 0xFFFF)
        payload += p32u((i*15) & 0xFFFFFFFF)
    # x = random.randint(1000,100000) / 100
    # y = random.randint(100,1000) / 100
    # print(x, y)

    payload += p8u(1)

    payload += pf64(32.0)
    payload += pf64(64.0)

    payload += p32u(32)
    payload += p8u(1)  # Bool
    payload += p8u(16)

    payload += p32u(501)
    payload += p32u(502)
    payload += p8u(15)
    payload += p32u(503)

    payload += p8u(102)
    payload += p8u(101)
    payload += p8u(100)
    payload += p8u(99)

    payload += p8u(0)  # Bool
    payload += p8u(1)  # Bool
    payload += p8u(1)  # Bool
    payload += p8u(1)  # Bool
    payload += p8u(1)  # Bool
    payload += p8u(1)  # Bool
    payload += p8u(1)  # Bool

    payload += p16u(400)
    payload += p16u(410)

    payload += p32u(700)
    payload += p8u(30)

    # these packets are send on else method..
    payload += p8u(1) # bool
    payload += p8u(1)
    payload += pstr("123456", 13)  # 13 bytes
    payload += p8u(12)
    payload += p8u(11)
    payload += p32u(600)
    payload += p8u(1)
    payload += p16u(430)
    payload += p16u(440)

    # for i in range(0,8000):
    #     payload += p8u(i % 0xFF)
    return csn.inject_payload(payload)