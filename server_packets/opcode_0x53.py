from lib import CSNSocket
from lib import p8, p16, p32, p64, p8u, p16u, p32u, p64u, pf32, pf64, pstr

import random


# Send UserNotFoundError
# case 0x53u:
#   CSNSocket::GetDataString(dword_57129C, v941, 17, a2, &v694, a3);
#   sprintf_s(v990, 0x80u, "%s%s", v941, "님은 서버에 없습니다.");
#   show_system_message(dword_5712B8, v990, -177017, 0);
#   return;
def opcode_53(username):

    payload = b"\x51"  # opcode 0x51
    payload += pstr(username, 17)
    return payload
