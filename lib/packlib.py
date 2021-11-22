import struct

def p8(x):
    return struct.pack('b', x)

def p8u(x):
    return struct.pack('B', x)

def p16(x):
    return struct.pack('h', x)

def p16u(x):
    return struct.pack('H', x)

def p32(x):
    return struct.pack('i', x)

def p32u(x):
    return struct.pack('I', x)

def p64(x):
    return struct.pack('q', x)

def p64u(x):
    return struct.pack('Q', x)

def pf32(x):
    return struct.pack('f', x)

def pf64(x):
    return struct.pack('d', x)

def pstr(x, size):
    return struct.pack('%ds' % size, bytes(x, encoding="euc-kr"))

def up8(x):
    return struct.unpack('b', x)[0]

def up8u(x):
    return struct.unpack('B', x)[0]

def up16(x):
    return struct.unpack('h', x)[0]

def up16u(x):
    return struct.unpack('H', x)[0]

def up32(x):
    return struct.unpack('i', x)[0]

def up32u(x):
    return struct.unpack('I', x)[0]

def up64(x):
    return struct.unpack('q', x)[0]

def up64u(x):
    return struct.unpack('Q', x)[0]

def upf32(x):
    return struct.unpack('f', x)[0]

def upf64(x):
    return struct.unpack('d', x)[0]

def upstr(x, size):
    return struct.unpack('%ds' % size, x)[0].decode('euc-kr')

