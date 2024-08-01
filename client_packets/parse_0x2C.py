from lib import CSNSocket
from lib import up32u, up16u, up8u


# Get List of Rooms
def parse_2C(payload: bytes):
    assert payload[0] == 0x2C
    code = int(payload[1])
    return code
