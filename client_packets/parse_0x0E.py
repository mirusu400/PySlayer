from lib import CSNSocket
from lib import up32u, up16u, up8u

# CreateUser <-> opcode_0x1C
def parse_0E(payload: bytes):
    assert payload[0] == 0x0E
    hair = up16u(payload[1:3])
    face = up16u(payload[3:5])
    shirt = up16u(payload[5:7])
    pants = up16u(payload[7:9])
    shoes = up16u(payload[9:11])
    name = payload[11:28].decode('euc_kr')
    rank = up8u(payload[28:29])
    _str = up16u(payload[29:31])
    _dex = up16u(payload[31:33])
    _int = up16u(payload[33:35])
    _tol = up16u(payload[35:37])
    print(f"[+] Create User: hair: {hair}, face: {face}, shirt: {shirt}, pants: {pants}, shoes: {shoes}, name: {name}, str: {_str}, dex: {_dex}, int: {_int}, tol: {_tol}")
    return