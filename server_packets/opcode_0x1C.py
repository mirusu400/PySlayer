from lib import CSNSocket
from lib import p8, p16, p32, p64, p8u, p16u, p32u, p64u, pf32, pf64, pstr

import random


# Create User
def opcode_1C() -> bytes:
    # csn = CSNSocket()
    payload = b"\x1C"  # opcode 0x14

    # Result Opcode
    # 0x01 = 정상 생성완료
    # 0x02 = 사용중인 이름입니다.\r\n다른 이름을 입력해 주세요.
    # 0x03 = 서버 처리중 입니다.\r\n잠시 후 다시 시도하시기 바랍니다.\r\n(DB)
    # 0x04 = 사용할 수 없는 이름입니다.\r\n다른 이름을 입력해주세요
    payload += p8(1)
    return payload
