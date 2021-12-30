from lib import CSNSocket
from lib import p8, p16, p32, p64, p8u, p16u, p32u, p64u, pf32, pf64, pstr

import random

# UseItem
def opcode_custom(opcode, datatype, data):

    payload = b""
    payload += p8u(opcode)  # case 1~5
    print(datatype)
    print(data)
    assert len(datatype) == len(data)
    for i in range(len(datatype)):
        if "p8" in datatype[i]:
            payload += p8(int(data[i]))
        elif "p16" in datatype[i]:
            payload += p16(int(data[i]))
        elif datatype[i] == "p32":
            payload += p32(int(data[i]))
        elif datatype[i] == "p64":
            payload += p64(int(data[i]))
        elif datatype[i] == "p8u":
            payload += p8u(int(data[i]))
        elif datatype[i] == "p16u":
            payload += p16u(int(data[i]))
        elif datatype[i] == "p32u":
            payload += p32u(int(data[i]))
        elif datatype[i] == "p64u":
            payload += p64u(int(data[i]))
        elif datatype[i] == "pf32":
            payload += pf32(float(data[i]))
        elif datatype[i] == "pf64":
            payload += pf64(float(data[i]))
        elif datatype[i] == "pstr":
            tstr = data[i].split("(")[0]
            length = int(data[i].split("(")[1].split(")")[0])
            payload += pstr(tstr[i], length)

    return payload