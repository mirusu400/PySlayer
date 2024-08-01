import sys

if __name__ == "__main__":
    key = b""
    xorkey = "xorKey = [\n"
    file = ""
    if len(sys.argv) != 2:
        print("Drag and Drop Fireway.dll file here.")
        file = input()
    else:
        file = sys.argv[1]
    with open(file, "rb") as f:
        f.seek(0x1E170)
        key = f.read(1024)

    if key[0] != 0x71:
        input("Please input correct Fireway.dll!")
        exit()

    for i in range(1024):
        xorkey += str(hex(key[i])) + ",\n"

    xorkey += "]\n"
    with open("_key.py", "w") as f:
        f.write(xorkey)
    input("Done!")
    exit()
