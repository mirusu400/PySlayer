from lib import CSNSocket
from lib import p8, p16, p32, p64, p8u, p16u, p32u, p64u, pf32, pf64, pstr

import random

# 놀이방 리스트 가져오기
def opcode_A1():
    playroom_count = 1
    payload = b"\xA1"
    payload += p8u(playroom_count) # 전체 룸 개수
    for i in range(playroom_count):
        payload += pstr("나혼자산다",17) # Roomname
        payload += p16u(1) 
        payload += p8u(8) # maxuser
        payload += p8u(4) # curruser
        payload += p8u(3) # ??
        payload += p8u(4) # ??
        payload += p16u(1) # ??
        payload += p8u(0) # IsLocked    
    return payload