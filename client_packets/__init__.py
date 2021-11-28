for i in range(0x00, 0xFF):
    try:
        exec("from .parse_0x%02X import parse_%02X" % (i, i))
    except:
        pass

# Load app functions into __all__
__all__ = [
    'parse_0D', 'parse_7E', 'parse_0B', 'parse_0C'
]