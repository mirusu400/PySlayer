from lib import CSNSocket
from lib import up32u

def parse_0D(payload: bytes):
    assert payload[0] == 0x0D
    
    return