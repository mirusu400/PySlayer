from lib import CSNSocket
from lib import up32u, up16u, up8u

# EquipItem
# Ex. Potion, Skill, Equip, etc..
def parse_0F(payload: bytes):
    assert payload[0] == 0x0D
    item = up16u(payload[1:3])
    if len(payload) > 3:
        unk1 = up8u(payload[3:4])
        unk2 = up16u(payload[4:6])
    return item