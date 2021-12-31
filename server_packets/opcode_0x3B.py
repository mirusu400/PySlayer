from lib import CSNSocket
from lib import p8, p16, p32, p64, p8u, p16u, p32u, p64u, pf32, pf64, pstr

import random

# UseSkills
def opcode_3B(skill:int, uid, time):

    payload = b"\x3B"
    payload += p16u(skill)
    payload += p8u(0) # If 1, add p32u (one more)
    payload += p32u(uid)
    payload += p16u(time)
    payload += p16u(time)
    # rand = 1
    
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