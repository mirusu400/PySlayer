from lib import CSNSocket
from lib import p8, p16, p32, p64, p8u, p16u, p32u, p64u, pf32, pf64, pstr
import random


# 파티맺기 거절문구
def opcode_56(reject_reason: int, username: str = ""):
    payload = b"\x56"
    # 1 = 파티원간 레벨차는 10이하여야 합니다.
    # 2 = sprintf(v969, "%s%s", &v912, "님이 파티맺기를 거절했습니다.");
    payload += p8(reject_reason)
    if reject_reason == 2:
        payload += pstr(username, 17)
    return payload
