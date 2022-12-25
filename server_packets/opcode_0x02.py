from lib import CSNSocket
from lib import p8, p16, p32, p64, p8u, p16u, p32u, p64u, pf32, pf64, pstr

# 캐릭터선택창 패킷
def opcode_02(uid, character_name, apparences):
    payload = b"\x02"
    payload += p8u(1)  # Must be 1
    payload += p32u(uid) # Character UID (Same as opcode_07)
    payload += p8u(100)
    payload += p8u(101)
    payload += p32u(123123)
    payload += p8u(6)
    payload += p8u(0)  # bool
    payload += p8u(1)  # len of characters

    for i in range(1):
        payload += pstr(character_name, 17) # Size 17
        payload += p8u(20)  # Bool (Must be zero)
        payload += p8u(1)
        payload += p8u(2)  # Job
        payload += p32u(0x0FFFFFFF)  # totalexp (For calculating level)
        payload += p32u(123456)
        payload += p32u(654321)
        payload += p32u(987987)
        payload += p32u(55)  # Delta ranking
        payload += p32u(6666)  # Delta ranking
        payload += p32u(7777)  # Delta ranking
        # payload += pstr("aa", 16) # Size 16
        # for i in [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1]:
        # # payload += pstr("\x01"*16,17)
        for j in [0, 0, 5, 3, 1]:
            payload += p8u(j)
        for j in [2, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]:
            payload += p8u(j)
        for j in apparences:  # About clothes
            payload += p16u(j)
    return payload
