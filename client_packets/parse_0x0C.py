from lib import CSNSocket
from lib import up32u, up16u, up8u


# Sell Item
def parse_0C(payload: bytes):
    assert payload[0] == 0x0C
    # ex. 0c54000100000000
    item = up16u(payload[1:3])
    count = up8u(payload[3:4])
    undef = up16u(payload[4:6])
    print(f"[+] Sell Item: item: {item}, count: {count}")

    return item, count
