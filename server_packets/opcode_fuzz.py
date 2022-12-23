from lib import CSNSocket
from lib import p8, p16, p32, p64, p8u, p16u, p32u, p64u, pf32, pf64, pstr
import string
import random

# Fuzz the opcode
def opcode_fuzz(opcode, datatype):

    payload = b""
    payload += p8u(opcode)  # case 1~5
    for i in range(len(datatype)):
        if "p8" in datatype[i]:
            if "u" in datatype[i]:
                payload += p8u(random.randint(0, 255))
            else:
                payload += p8(random.randint(-128, 127))
        elif "p16" in datatype[i]:
            if "u" in datatype[i]:
                payload += p16u(random.randint(0, 65535))
            else:
                payload += p16(random.randint(-32768, 32767))
        elif "p32" in datatype[i]:
            if "u" in datatype[i]:
                payload += p32u(random.randint(0, 4294967295))
            else:
                payload += p32(random.randint(-2147483648, 2147483647))
        elif "p64" in datatype[i]:
            if "u" in datatype[i]:
                payload += p64u(random.randint(0, 18446744073709551615))
            else:
                payload += p64(random.randint(-9223372036854775808, 9223372036854775807))
        elif datatype[i] == "pf32":
            payload += pf32(random.uniform(-3.4028234663852886e+38, 3.4028234663852886e+38))
        elif datatype[i] == "pf64":
            payload += pf64(random.uniform(-1.7976931348623157e+308, 1.7976931348623157e+308))
        elif datatype[i].startswith("pstr"):
            data = datatype[i]
            length = int(data[i].split("(")[1].split(")")[0])
            # get random string
            tstr = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(length-1))
            payload += pstr(tstr, length)

    return payload