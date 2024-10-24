from lib import CSNSocket
from lib import p8, p16, p32, p64, p8u, p16u, p32u, p64u, pf32, pf64, pstr

import random


# case 0xD6u:
#   CSNSocket::GetDataU8(dword_57129C, (char *)&v723 + 3, a2, &v694, a3);
#   sprintf_s(v987, 0x80u, "%d레벨이상인 캐릭터만 갈 수 있는\r\n지역입니다.", HIBYTE(v723));
#   show_system_dialog(v987, (_DWORD *)dword_5712B8, 3, 3, 0, 0);
#   return;
def opcode_D6(level):

    payload = b"\xD6"
    # %d레벨이상인 캐릭터만 갈 수 있는\r\n지역입니다.
    payload += p8(level)
    return payload
