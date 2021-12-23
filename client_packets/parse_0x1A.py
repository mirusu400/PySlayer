from lib import up32u, up16u, up8u
# ex. 1a010001


# EquipItem
def parse_1A(payload: bytes):
    assert payload[0] == 0x1a
    unk1 = up16u(payload[1:2])
    unk2 = (payload[3])
    return unk1, unk2