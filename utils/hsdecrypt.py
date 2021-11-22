# Decrypt all of hm* files
# .hsc => Hamelin Sprite Archive (DDS texture file)
# .hmi => Hamelin Map Info
# .hsi => Hamelin Sprite Info
# .hqi => Hamelin Quest Info
# .hki => Hamelin  Skill Info (Because you press'k' to open the skills menu in most Korean MMOs)
# .hui => Hamelin User-interface Info
# .hii => Hamelin Item Info
# .hni => Hamelin NPC Info
# .hbi => Unknown / "Welcome to WindSlayer2 Closed Beta Testing!" (?)
# .hci => Unknown / "Number of motions" with a bunch of u64s
# .hpi => Unknown / Korean string with 2 u8s.
# .lng => Language Mapping / Maps ints to English strings, probably referenced by every other datafile for regional translation convenience. Prefixed by what the strings are related to i.e. ("UI", "ITM", etc).
# Written by mirusu400
import zipfile
import sys


def decode(payload):
    p = []
    for idx in range(0,len(payload)):
        if idx % 3 == 1:
            dec = (payload[idx] + 0xDD + 1) & 0xFF
        elif idx % 3 == 2:
            dec = (payload[idx] + 0xDF + 1) & 0xFF
        else:
            dec = (payload[idx] + 0xE8 + 1) & 0xFF
        p.append(dec)
    return bytes(p)


if __name__ == "__main__":
    filename = sys.argv[1]

    if "hsc" in filename:
        myzip_r = zipfile.ZipFile(filename, 'r')
        temp_file = myzip_r.read("temp_file")
        tp2 = decode(temp_file)
        with open(f"{filename}.dds", "wb") as f:
            f.write(tp2)
    else:
        with open(filename, "rb") as f:
            payload = f.read()
            payload = decode(payload)
        with open(f"{filename}.out", "wb") as f:
            f.write(payload)  