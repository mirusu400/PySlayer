from lib import CSNSocket
from lib import p8, p16, p32, p64, p8u, p16u, p32u, p64u, pf32, pf64, pstr
import sqlite3
import random

# Ingame Init packet
def opcode_07(uid, charactername, job1, job2, _str, _dex, _int, _tol, level,
    hp, mp, equips, apparences, xpos=500, ypos=500) -> bytes:
    
    payload = b"\x07"  # opcode 7
    v802 = 1
    payload += p8u(v802+1)  # Must be >= 1
    for i in range(v802):
        payload += pstr(charactername, 17)
        payload += p32u(uid)  # Unique Character opcode, must be >= 2
        payload += p32u(1)
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
        payload += p8u(job1) # 1차 전직
        payload += p8u(job2) # 2차 전직
        # payload += p16u(12)
        payload += p8u(level)  # Level
        payload += p8u(20) # 계급

        payload += p8u(30)  # 성별?

        for i in apparences:  # 외형 (loop 17)
            payload += p16u(i)

        payload += p16u(_str)  # 힘
        payload += p16u(_dex)  # 민첩
        payload += p16u(_int)  # 지혜
        payload += p16u(_tol)  # 근성

        for i in equips:  # Equip (loop 15)
            payload += p16u(i)
            for j in range(0, 6): # Equip enchant
                payload += p16u(0)
        # line 1874

        for i in range(0, 10): # Cash Equip
            payload += p16(0) # Item Id
            payload += p16(0)   # 속성부여아이템 ID
            payload += p16(0)   # 속성부여아이템 ID

        # line 1886
        payload += p8u(0)
        # Buff things
        # for i in [88, 90, 94, 0x15B]:
        #     payload += p16u(1)
        # print(x, y)

        payload += p8u(0)

        payload += pf64(xpos)
        payload += pf64(ypos)

        payload += p32u(32)
        payload += p8u(0)  # Bool
        payload += p8u(1)

        payload += p32u(501)
        payload += p32u(502)
        payload += p8u(100)
        payload += p32u(503)

        payload += p8u(0)
        payload += p8u(0)
        payload += p8u(0)
        payload += p8u(0)

        payload += p8u(0)  # Bool
        payload += p8u(0)  # Bool
        payload += p8u(0)  # Bool
        payload += p8u(0)  # Bool
        payload += p8u(0)  # Bool
        payload += p8u(0)  # Bool
        payload += p8u(0)  # Bool

        payload += p16u(hp) # HP
        payload += p16u(mp) # MP

        payload += p32u(1)
        payload += p8u(1)

        # these packets are send on else method..
        # payload += p8u(1) # bool
        # payload += p8u(1)
        # payload += pstr("123456789", 13)  # 13 bytes
        # payload += p8u(1)
        # payload += p8u(1)
        # payload += p32u(800)
        # payload += p8u(1)
        # payload += p16u(101)
        # payload += p16u(101)

        # for i in range(0,8000):
        #     payload += p8u(i % 0xFF)
    payload += dummy()
    return payload



def dummy():
    payload = pstr("테스트용", 17)
    payload += p32u(10)  # Unique Character opcode, must be >= 2
    payload += p32u(1)
    payload += p16u(1)  # If 1, send packet below:

    payload += p8u(2)
    payload += pstr("응애", 17)

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
    payload += p8u(2) # 2차 전직
    # payload += p16u(12)
    payload += p8u(10)  # Level
    payload += p8u(20) # 계급

    payload += p8u(30)  # 성별?

    for i in [0, 123, 0, 0, 125, 113, 110, 0, 116, 131, 0, 10, 0, 701, 701, 701, 701]:  # 외형 (loop 17)
        payload += p16u(i)

    payload += p16u(1)  # 힘
    payload += p16u(1)  # 민첩
    payload += p16u(1)  # 지혜
    payload += p16u(1)  # 근성

    for i in [100, 100, 100, 100, 101, 3020, 100, 100, 100, 100, 100, 100, 100, 100, 100]:  # Equip (loop 15)
        payload += p16u(i)
        for j in range(0, 6): # Equip enchant
            payload += p16u(0)
    # line 1874

    for i in range(0, 10): # Cash Equip
        payload += p16(0) # Item Id
        payload += p16(0)   # 속성부여아이템 ID
        payload += p16(0)   # 속성부여아이템 ID

    # line 1886
    payload += p8u(0)
    # Buff things
    # for i in [88, 90, 94, 0x15B]:
    #     payload += p16u(1)
    # print(x, y)

    payload += p8u(0)

    payload += pf64(645)
    payload += pf64(1506)

    payload += p32u(32)
    payload += p8u(0)  # Bool
    payload += p8u(1)

    payload += p32u(501)
    payload += p32u(502)
    payload += p8u(100)
    payload += p32u(503)

    payload += p8u(0)
    payload += p8u(0)
    payload += p8u(0)
    payload += p8u(0)

    payload += p8u(0)  # Bool
    payload += p8u(0)  # Bool
    payload += p8u(0)  # Bool
    payload += p8u(0)  # Bool
    payload += p8u(0)  # Bool
    payload += p8u(0)  # Bool
    payload += p8u(0)  # Bool

    payload += p16u(100) # HP
    payload += p16u(100) # MP

    payload += p32u(1)
    payload += p8u(1)

    # these packets are send on else method..
    payload += p8u(1) # bool
    payload += p8u(1)
    payload += pstr("123456789", 13)  # 13 bytes
    payload += p8u(1)
    payload += p8u(1)
    payload += p32u(800)
    payload += p8u(1)
    payload += p16u(101)
    payload += p16u(101)
    return payload