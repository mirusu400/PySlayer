from lib import CSNSocket
from lib import up32u
map_data = {
    13: {"map_name": "발데란", "map_file_code": 701},
    20: {"map_name": "포폴라마을", "map_file_code": 201}, # Originally, it gotes to before map (벼룩시장 포탈)
    45: {"map_name": "오행산가는길", "map_file_code": 418},
    51: {"map_name": "포폴라마을", "map_file_code": 201},
    65: {"map_name": "발데란", "map_file_code": 701},
    181: {"map_name": "포폴라마을", "map_file_code": 201},
    162: {"map_name": "포폴라언덕2", "map_file_code": 106},
    142: {"map_name": "오행산입구", "map_file_code": 419},
    144: {"map_name": "오지촌샛길2", "map_file_code": 422},
    177: {"map_name": "아마쿠사", "map_file_code": 501},
    184: {"map_name": "벼룩시장", "map_file_code": 9701},
    222: {"map_name": "벼룩시장", "map_file_code": 9701},

}
def parse_7E(payload: bytes):
    assert payload[0] == 0x7E
    mapcode = up32u(payload[1:5])
    print(f"[*] Find mapcode: {mapcode}")
    try:
        return map_data[mapcode]["map_file_code"]
    except KeyError:
        print(f"[-] Undefined mapcode: {mapcode}")
        return 401
    return