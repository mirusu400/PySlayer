from lib import CSNSocket
from lib import p8, p16, p32, p64, p8u, p16u, p32u, p64u, pf32, pf64, pstr

import random


# UseItem
def opcode_AE(code):

    payload = b"\xAE"
    payload += p8(1)  # case 1~5
    payload += p16(code)
    # case 3 : ??
    # case 4 : 같은 필드에 당신의 모닥불 ~
    # case 5 : 같은 아이템을 이미 사용중입니다.
    # payload += p16u(code) #??
    return payload
