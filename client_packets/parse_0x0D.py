from lib import CSNSocket
from lib import up32u, upf64

def parse_0D(payload: bytes):
    assert payload[0] == 0x0D
    xpos = upf64(payload[3:11])
    ypos = upf64(payload[11:19])
    return (xpos, ypos)