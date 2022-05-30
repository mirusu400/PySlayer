from lib import CSNSocket
from lib import p8, p16, p32, p64, p8u, p16u, p32u, p64u, pf32, pf64, pstr
import sqlite3
import random

# CharacterReset?
def opcode_2E(character_name, job1, job2, _str, _dex, _int, _tol, level,
    hp, mp, equips, apparences, xpos=500, ypos=500) -> bytes:
    
    payload = b"\x2B"  # opcode 2E
    v802 = 1
    payload += p8u(v802)  # Must be >= 1
    for i in range(v802):
        payload += pstr(character_name, 17)
        payload += p32u(10)  # Must be 2
        payload += p32u(30)
        payload += p16u(0)  # If 1, send packet below:
        # Pstr(17) p16 p16
        # payload += p8u(2)
        # payload += pstr("나혼자산다", 17)

        # If >1, send packet below{str 16 16}:
        # If ==1, Bool
        # Guild info
        payload += p8u(0)
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

        # === end if
        # 4 == 도적 ( 2 == 트랩퍼)
        # 5 == 마법사
        # 6 == 사제
        payload += p8u(job1) # 1차 전직
        payload += p8u(job2) # 2차 전직
        # payload += p16u(12)
        payload += p8u(level)  # Level
        payload += p8u(20) # 계급

        payload += p8u(1)  # Bool

        for i in apparences:  # 외형 (loop 17)
            payload += p16u(i)

        payload += p16u(_str)  # 힘
        payload += p16u(_dex)  # 민첩
        payload += p16u(_int)  # 지혜
        payload += p16u(_tol)  # 근성
        payload += p16u(100)
        payload += p16u(101)

        for i in equips:  # Equip (loop 15)
            payload += p16u(i)
            for j in range(0, 6): # Equip enchant
                payload += p16u(0)
        # line 1874

        for i in range(0, 10): # Cash Equip
            payload += p16(100) # Item Id
            payload += p16(1)   # 속성부여아이템 ID
            payload += p16(1)   # 속성부여아이템 ID

        # line 4188
        payload += p8u(0)
        # Buff things
        # for i in [88, 90, 94, 0x15B]:
        #     payload += p16u(1)
        
        # 4225
        payload += p8u(0) # Something
    
        payload += p8u(1)
        payload += p8u(2)
        payload += p8u(3)
        payload += p32u(100)

        # Else method
        payload += p8u(0) # Bool
        payload += p8(1)
        payload += pstr("test",13)
        # for i in range(0,8000):
        #     payload += p8u(i % 0xFF)
    return payload