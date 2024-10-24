from lib import CSNSocket
from lib import p8, p16, p32, p64, p8u, p16u, p32u, p64u, pf32, pf64, pstr

import random


# Detailed chatting packet
def opcode_15(chat_type: int, string1: str, string2: str):
    payload = b"\x15"
    # 0 == 시안
    # 1 == 연두~파랑 사이
    # 2 == 초록색
    # 3 == [%s]길드와 [%s]길드의 경기가 시작 되었습니다.
    # 4 == [%s]길드가 [%s]길드와의 경기에서 승리 하였습니다.
    # 5 == [%s]길드와 [%s]길드의 경기가 무승부로 끝났습니다
    payload += p8u(chat_type)
    if chat_type < 3:
        length = string1.encode("euc-kr").__len__()
        payload += p8u(length)
        payload += pstr(string1, length)
    else:
        # [%s] 길드와 [%s] <- 이거읟 ㅜ string
        payload += pstr(string1, 17)
        payload += pstr(string2, 17)
    return payload
