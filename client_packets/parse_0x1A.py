from lib import up32u, up16u, up8u

# ex. 1a010001


# EquipItem
def parse_1A(payload: bytes):
    assert payload[0] == 0x1A
    room_num = up16u(payload[1:3])
    room_person_count = payload[3]
    return room_num, room_person_count
