import struct


def p8(x) -> bytes:
    return struct.pack("b", x)


def p8u(x) -> bytes:
    return struct.pack("B", x)


def p16(x) -> bytes:
    return struct.pack("h", x)


def p16u(x) -> bytes:
    return struct.pack("H", x)


def p32(x) -> bytes:
    return struct.pack("i", x)


def p32u(x) -> bytes:
    return struct.pack("I", x)


def p64(x) -> bytes:
    return struct.pack("q", x)


def p64u(x) -> bytes:
    return struct.pack("Q", x)


def pf32(x) -> bytes:
    return struct.pack("f", x)


def pf64(x) -> bytes:
    return struct.pack("d", x)


def pstr(x, size) -> bytes:
    return struct.pack("%ds" % size, bytes(x, encoding="euc-kr"))


def up8(x) -> int:
    return struct.unpack("b", x)[0]


def up8u(x) -> int:
    return struct.unpack("B", x)[0]


def up16(x) -> int:
    return struct.unpack("h", x)[0]


def up16u(x) -> int:
    return struct.unpack("H", x)[0]


def up32(x) -> int:
    return struct.unpack("i", x)[0]


def up32u(x) -> int:
    return struct.unpack("I", x)[0]


def up64(x) -> int:
    return struct.unpack("q", x)[0]


def up64u(x) -> int:
    return struct.unpack("Q", x)[0]


def upf32(x) -> float:
    return struct.unpack("f", x)[0]


def upf64(x) -> float:
    return struct.unpack("d", x)[0]


def upstr(x, size) -> str:
    return struct.unpack("%ds" % size, x)[0].decode("euc-kr")
