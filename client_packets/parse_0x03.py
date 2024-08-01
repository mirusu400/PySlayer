from lib import CSNSocket
from lib import up32u, up16u, up8u


# Chatting
def parse_03(payload: bytes):
    assert payload[0] == 0x03
    length = payload[1]
    text = payload[2 : 2 + length].decode("euc-kr")

    return length, text
