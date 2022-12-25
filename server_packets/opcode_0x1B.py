from lib import CSNSocket
from lib import p8, p16, p32, p64, p8u, p16u, p32u, p64u, pf32, pf64, pstr
import sqlite3
import random

# Mob get damage
def opcode_1B(mob_uid, damage, wtf: str) -> bytes:
    payload = b"\x1B"  # opcode 1B
    payload += p32u(mob_uid)
    payload += p32u(damage)
    payload += pstr(wtf, 8)
    return payload
