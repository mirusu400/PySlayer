import json


def find_nth(haystack, needle, n):
    start = haystack.find(needle)
    while start >= 0 and n > 1:
        start = haystack.find(needle, start + len(needle))
        n -= 1
    return start


def parse_hsi_to_dict(items):
    images_datas = []
    sprite_datas = []
    for line in items:
        data = {}
        line = line.replace("\n", "").replace(": ", ":")
        idx = -1
        try:
            title_idx = line.split(" ")[1]
            data["Title_Idx"] = title_idx
        except:
            pass
        try:
            idx = int(line.split(" ")[0])
        except:
            pass
        if idx == -1:
            start = 0
        else:
            start = find_nth(line, " ", 2)
            # start = line.find(" ")+1
        mode = "str"
        temp_key = ""
        temp_value = ""
        if len(line.split(" ")) == 2:
            temp_key = line.split(" ")[0]
            temp_value = line.split(" ")[1]
            images_datas.append({"idx": temp_key, "path": temp_value})
        else:
            while True:
                if mode == "str":
                    if line[start] == ":":
                        mode = "key"
                    else:
                        temp_key += line[start]
                else:
                    if line[start] == " ":
                        if start == len(line) - 1:
                            data["idx"] = idx
                            data[temp_key.strip()] = temp_value.strip()
                            break
                        elif ord("A") <= ord(line[start + 1]) and ord(
                            line[start + 1]
                        ) <= ord("z"):
                            mode = "str"
                            data["idx"] = idx
                            data[temp_key.strip()] = temp_value.strip()
                            temp_key = ""
                            temp_value = ""
                        else:
                            temp_value += line[start]
                    else:
                        temp_value += line[start]
                start += 1
                if start >= len(line):
                    break
            sprite_datas.append(data)
    return images_datas, sprite_datas


if __name__ == "__main__":
    images = {}
    sprites = {}
    with open("./windslayer.hqi.txt", "r", encoding="utf-8") as f:
        items = f.readlines()
        images, sprites = parse_hsi_to_dict(items)
    with open("./images.json", "w", encoding="utf-8") as f:
        json.dump(images, f, ensure_ascii=False, indent=4)
    with open("./sprites.json", "w", encoding="utf-8") as f:
        json.dump(sprites, f, ensure_ascii=False, indent=4)
