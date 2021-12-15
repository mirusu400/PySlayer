from lib import CSNSocket
from lib import p8, p16, p32, p64, p8u, p16u, p32u, p64u, pf32, pf64, pstr

import random

# UseItem
def opcode_D7(code):

    payload = b"\xD7"
    payload += p8(3)  # case 1~5
    payload += pstr("test", 17)
    # case 3 : ??
    # case 4 : 같은 필드에 당신의 모닥불 ~
    # case 5 : 같은 아이템을 이미 사용중입니다.
    # payload += p16u(code) #??
    return payload