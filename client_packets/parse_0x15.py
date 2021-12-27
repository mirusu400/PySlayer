from lib import CSNSocket
from lib import up32u, up16u, up8u

# UseItem
# Ex. Potion, Skill, etc..
def parse_15(payload: bytes):
    assert payload[0] == 0x15
    item = up16u(payload[1:3])
    return item