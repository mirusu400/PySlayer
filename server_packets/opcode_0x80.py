from lib import CSNSocket
from lib import p8, p16, p32, p64, p8u, p16u, p32u, p64u, pf32, pf64, pstr

import random


# About Cash??
def opcode_80():

    payload = b"\x80"
    #       CSNSocket::GetDataU8(dword_57129C, (char *)&v724 + 3, a2, &v694, a3);
    #       if ( HIBYTE(v724) != 1 )
    #       {
    # LABEL_93:
    #         show_system_dialog(
    #           "잘못된 인증번호입니다.\r\n\r\n인증번호 확인 후 다시 시도해 주세요.",
    #           (_DWORD *)dword_5712B8,
    #           3,
    #           3,
    #           0,
    #           0);
    #         return;
    #       }
    payload += p8(1)
    # 0x!f9, 0x4CF, 0x1FA, 0x4B8
    payload += p32u(0x4CF)
    return payload
