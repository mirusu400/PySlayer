from lib import CSNSocket
from lib import p8, p16, p32, p64, p8u, p16u, p32u, p64u, pf32, pf64, pstr

import random


# Unused?
# case 0x17u:
#   v5[1653] = 1;
#   return;
def opcode_17():
    # 아무것도 안함
    #
    payload = b"\x17"
    return payload
