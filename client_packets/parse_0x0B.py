from lib import CSNSocket
from lib import up32u, up16u, up8u

# Buy Item
def parse_0B(payload: bytes):
    assert payload[0] == 0x0B
    item = up16u(payload[1:3])
    count = up8u(payload[3:4])
    undef = up16u(payload[4:6])
    print(f'[+] Buy Item: item: {item}, count: {count}')
    
    return item, count