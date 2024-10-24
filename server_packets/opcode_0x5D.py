from lib import CSNSocket
from lib import p8, p16, p32, p64, p8u, p16u, p32u, p64u, pf32, pf64, pstr

import random


# Force game quit (해킹 감지 등)
def opcode_5D(quit_reason: int):
    payload = b"\x5D"
    # 1 = "비정상적인 게임진행으로 접속을 끊습니다"
    # 2 = "비정상적인 게임입력시간으로 접속을 끊습니다"
    # 3 = "자동 사냥으로 판명되어 접속을 끊습니다"
    # 4 = "관리자의 요청에 의해 게임을 종료합니다"
    # 0x63 = "서버로의 전송이 실패하였습니다"
    # default = "서버와의 접속이 끊어졌습니다"
    payload += p8(quit_reason)
    return payload
