# from .packet_0x01 import opcode_01
# from .packet_0x02 import opcode_02
# from .packet_0x03 import opcode_03
# from .packet_0x04 import opcode_04

# from .packet_0x07 import opcode_07
# from .packet_0x08 import opcode_08

# from .packet_0x13 import opcode_13
# from .packet_0x14 import opcode_14

# from .packet_0xA5 import opcode_A5

for i in range(0x00, 0xFF):
    try:
        exec("from .packet_0x%02X import opcode_%02X" % (i, i))
    except:
        pass

# Load app functions into __all__
__all__ = [
    'opcode_01', 'opcode_02', 'opcode_03', 'opcode_04', 'opcode_07', 'opcode_08',
    'opcode_13', 'opcode_14', 'opcode_A5', 'opcode_2F', 'opcode_19',
    'opcode_18', 'opcode_26', 'opcode_59', 'opcode_28', 'opcode_51', 'opcode_29',
    'opcode_80', 'opcode_D7', 'opcode_AE', 'opcode_99', 'opcode_25', 'opcode_05'
]