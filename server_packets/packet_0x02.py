from lib import CSNSocket
from lib import p8, p16, p32, p64, p8u, p16u, p32u, p64u, pf32, pf64, pstr

def opcode_02():

    payload = b"\x02"
    payload += p8u(1)  # Must be 1
    payload += p32u(2)
    payload += p8u(3)
    payload += p8u(4)
    payload += p32u(5)
    payload += p8u(6)
    payload += p8u(1)  # bool
    payload += p8u(1)  # len of characters

    for i in range(0, 1):
        payload += b"mirusu400012345\0"  # Size 17
        payload += p8u(0)  # Bool (Must be zero)
        payload += p8u(1)
        payload += p16u(9)  # Job
        payload += p32u(987654)  # totalexp
        payload += p32u(665)
        payload += p32u(666)
        payload += p32u(667)
        payload += p32u(30)  # Delta ranking
        payload += p32u(40)  # Delta ranking
        payload += p32u(50)  # Delta ranking
        # payload += b"012345678901234\0" # size 16

        # for i in [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1]:
        # payload += pstr("\x01"*16,17)
        for i in [0, 0, 0, 1]:
            payload += p8u(i)
        payload += p8u(0)  # Must be 0, if 1, character removed.
        for i in [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1]:
            payload += p8u(i)
        for i in range(0, 17):  # About clothes
            payload += p16u(120 + i)
    return payload
