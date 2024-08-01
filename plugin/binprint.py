class BinPrint:
    def __init__(self, bin_str=None, encode="utf-8", width=0x10):
        self.bin_str = None
        self.width = width
        # print_width = hex width + ascii width + offset width + etc
        self.print_width = (width * 3) + width + 0x8 + 0x3 + 0x3

        if bin_str:
            self.set_data(bin_str, encode)

    def set_data(self, data, encode):
        if type(data) == bytes:
            self.bin_str = data
        elif type(data) == str:
            self.bin_str = data.encode(encoding=encode)

    def print(self):
        print("-" * self.print_width)
        buffer = self.bin_str

        offset = 0
        while offset < len(buffer):
            # Offset
            print(" %08X | " % (offset), end="")
            if ((len(buffer) - offset) < self.width) is True:
                data = buffer[offset:]
            else:
                data = buffer[offset : offset + self.width]

            # Hex Dump
            for hex_dump in data:
                print("%02X" % hex_dump, end=" ")

            if ((len(buffer) - offset) < self.width) is True:
                print(" " * (3 * (self.width - len(data))), end="")

            print("  ", end="")

            # Ascii
            for ascii_dump in data:
                if ((ascii_dump >= 0x20) is True) and ((ascii_dump <= 0x7E) is True):
                    print(chr(ascii_dump), end="")
                else:
                    print(".", end="")

            offset = offset + len(data)
            print()

        print("-" * self.print_width)
