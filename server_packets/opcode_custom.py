from lib import CSNSocket
from lib import p8, p16, p32, p64, p8u, p16u, p32u, p64u, pf32, pf64, pstr

import random

# UseItem
def opcode_custom(opcode, datatype, data):

    payload = b""
    payload += p8u(opcode)  # case 1~5
    assert len(datatype) == len(data)
    for i in range(len(datatype)):
        if datatype == "p8":
            payload += p8(data[i])
        elif datatype == "p16":
            payload += p16(data[i])
        elif datatype == "p32":
            payload += p32(data[i])
        elif datatype == "p64":
            payload += p64(data[i])
        elif datatype == "p8u":
            payload += p8u(data[i])
        elif datatype == "p16u":
            payload += p16u(data[i])
        elif datatype == "p32u":
            payload += p32u(data[i])
        elif datatype == "p64u":
            payload += p64u(data[i])
        elif datatype == "pf32":
            payload += pf32(data[i])
        elif datatype == "pf64":
            payload += pf64(data[i])
        elif datatype == "pstr":
            tstr = data[i].split("(")[0]
            length = int(data[i].split("(")[1].split(")")[0])
            payload += pstr(tstr[i], length)

    return payload