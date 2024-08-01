from lib import CSNSocket
from lib import p8, p16, p32, p64, p8u, p16u, p32u, p64u, pf32, pf64, pstr
import string
import random
import time
from copy import deepcopy


# Fuzz the opcode
def opcode_fuzz(opcode, payload_dict: dict):

    types = payload_dict["types"]
    defaults = deepcopy(payload_dict["default"])
    payload = b""
    payload += p8u(opcode)  # case 1~5
    random.randint(0, 255)
    for i in range(len(defaults)):
        if "-" in defaults[i]:
            defaults[i] = random.randint(
                int(defaults[i].split("-")[0]), int(defaults[i].split("-")[1])
            )
        if defaults[i] == "rand":
            if "p8" in types[i]:
                if "u" in types[i]:
                    defaults[i] = random.randint(0, 255)
                else:
                    defaults[i] = random.randint(-128, 127)
            elif "p16" in types[i]:
                if "u" in types[i]:
                    defaults[i] = random.randint(0, 65535)
                else:
                    defaults[i] = random.randint(-32768, 32767)
            elif "p32" in types[i]:
                if "u" in types[i]:
                    defaults[i] = random.randint(0, 4294967295)
                else:
                    defaults[i] = random.randint(-2147483648, 2147483647)
            elif "p64" in types[i]:
                if "u" in types[i]:
                    defaults[i] = random.randint(0, 18446744073709551615)
                else:
                    defaults[i] = random.randint(
                        -9223372036854775808, 9223372036854775807
                    )
            elif "pf32" in types[i]:
                defaults[i] = random.uniform(-2147483648, 2147483647)
            elif "pf64" in types[i]:
                defaults[i] = random.uniform(-9223372036854775808, 9223372036854775807)

            elif types[i].startswith("pstr"):
                data = types[i]
                length = int(data[i].split("(")[1].split(")")[0])
                # get random string
                tstr = "".join(
                    random.choice(string.ascii_uppercase + string.digits)
                    for _ in range(length - 1)
                )
                payload += pstr(tstr, length)
        else:
            defaults[i] = int(defaults[i])
    print(defaults)
    for i in range(len(defaults)):
        if "p8" in types[i]:
            if "u" in types[i]:
                payload += p8u(defaults[i])
            else:
                payload += p8(defaults[i])
        elif "p16" in types[i]:
            if "u" in types[i]:
                payload += p16u(defaults[i])
            else:
                payload += p16(defaults[i])
        elif "p32" in types[i]:
            if "u" in types[i]:
                payload += p32u(defaults[i])
            else:
                payload += p32(defaults[i])
        elif "p64" in types[i]:
            if "u" in types[i]:
                payload += p64u(defaults[i])
            else:
                payload += p64(defaults[i])
        elif "pf32" in types[i]:
            payload += pf32(defaults[i])
        elif "pf64" in types[i]:
            payload += pf64(defaults[i])
        elif types[i].startswith("pstr"):
            data = types[i]
            length = int(data[i].split("(")[1].split(")")[0])
            payload += pstr(defaults[i], length)
    return payload
