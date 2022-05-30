from lib import CSNSocket
from lib import up32u, up16u, up8u, upstr

# Ingame Welcome packet


def parse_2B(payload: bytes):
    assert payload[0] == 0x2B
    ip = upstr(payload[0x06:0x15], 15).replace("\x00","").replace("\r","").replace("\n","").strip()
    print(f'[+] Ip address: {ip}')

    return ip
