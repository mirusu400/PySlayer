from lib import CSNSocket
from lib import p8, p16, p32, p64, p8u, p16u, p32u, p64u, pf32, pf64, pstr

import random


# Changemap packet
def opcode_08(map_file_code, uid):

    payload = b"\x08"
    # 0x1 == PVP 서버와 연결이 끊어졌습니다. 인터넷 연결을 확인해 주세요.
    # 0x2 == 방장에의해 강퇴되었습니다.
    # 0x3 == 부적절한 방제목 사용으로\n방이 삭제되었습니다.\n이와같은 방을 이용하게 될 경우\n불이익을 당할 수 있으니 주의하세요
    # 0x4 == 부적절한 방제목 사용으로\n방을 개설 하셨습니다.\n매너 점수가 삭감됩니다.
    # 0x5 == 해킹툴을 사용하였습니다.\n이 정보는 누적기록되며,\n이로 인한 불이익을 당할 수 있습니다.

    payload += p8u(0)
    payload += p16u(map_file_code)
    payload += p32u(uid)  # wtf is this?
    payload += p32u(0)  # 누적플탐
    return payload
