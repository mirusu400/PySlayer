from lib import up32u, up16u, up8u

# 전장 대기표
def parse_39(payload: bytes):
    assert payload[0] == 0x39
    fight_type = up8u(payload[1:2])
    return fight_type