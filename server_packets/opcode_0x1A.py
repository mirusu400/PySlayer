from lib import CSNSocket
from lib import p8, p16, p32, p64, p8u, p16u, p32u, p64u, pf32, pf64, pstr
import sqlite3
import random

# Mob about packet
def opcode_1A(npccode) -> bytes:
    payload = b"\x1A"  # opcode 1A
    xpos = float(input("xpos?"))
    ypos = float(input("ypos?"))
    v748 = 1
    uid = 0xFFFF + 1
    # xpos = 398
    # ypos = 450
    payload += p8u(v748)  # Must be >= 1
    for i in range(v748):
        payload += p32u(npccode)
        payload += p32u(uid) # player uid

        ### Some big routine here...

        loop1 = 0
        payload += p8u(loop1) # About buff

        for i in range(loop1):
            payload += p16u(1) # Buff Code
            payload += p32u(1) # User?

        loop2 = 0
        payload += p8u(loop2)

        for i in range(loop2):
            payload += p8u(1)
        payload += pf64(xpos)
        payload += pf64(ypos)

        # sub_428180

        payload += p8u(0)
        payload += p8u(0)

        payload += p32u(0)
        payload += p32u(0)
        payload += p32u(0)
        payload += p32u(0)
        payload += p32u(0)
        payload += p32u(0)


        payload += p8u(0) # Bool
        payload += p8u(0)

        payload += p32u(1)
        payload += p32u(1)

        payload += p8u(0)
        payload += p32u(0)

        payload += p8u(0)
        payload += p8u(0)
        payload += p8u(0)
        payload += p8u(0)
        
        payload += p8u(0) # Bool
        payload += p8u(0) # Bool
        payload += p8u(0) # Bool
        payload += p8u(0) # Bool
        payload += p8u(0) # Bool
        payload += p8u(0) # Bool
        payload += p8u(0) # Bool
        
        payload += p16u(202) # ??

        payload += p32u(1)

        check = 0 # 어그로?
        payload += p8u(check)
        if check:
            payload += p32u(1)
            payload += p32u(1)

        print(payload)
        return payload
