from lib import CSNSocket
from lib import up16u, up32u, upf64
import binascii


def parse_0D(payload: bytes):
    assert payload[0] == 0x0D
    undef = up32u(payload[1:5])
    sub_opcode = up16u(payload[5:7])  # Must be 00 C9?
    sub_opcode2 = up16u(payload[7:9])  # Maybe hash? Idk...
    if sub_opcode2 == 0xD2:  # Move packet
        return
    unk = up32u(payload[0x0D:0x11])
    unk2 = up16u(payload[0x11:0x13])
    keycode = payload[0x0B]

    # print(binascii.hexlify(payload))

    return
