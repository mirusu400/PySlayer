from PIL import Image
import json
import os
import openpyxl as op
#엑셀 이미지 삽입을 위한 openpyxl import
from openpyxl.drawing.image import Image as Img

images = [
    Image.open("./item/item001_a1.hsc.dds"),
    Image.open("./item/item002_a0.hsc.dds"),
    Image.open("./item/item003_a1.hsc.dds"),
    Image.open("./item/item004_a1.hsc.dds")
]
with open("./sprites.json", "r", encoding="utf-8") as f:
    sprites = json.load(f)

with open("./ITMLng/ITMLngKo.lng.json", "r", encoding="utf-8") as f:
    lng = json.load(f)

save_path = "items.xlsx"
wb = op.Workbook()
ws = wb.active

idx = 2
ws.append(["idx", "name", "desc", "type", "hp", "mp", "icon"])
for item in lng:
    spridx = item["sprite"]
    img = 0
    x1 = y1 = x2 = y2 = 0

    for spr in sprites:
        if spr["idx"] == spridx:
            img = int(spr["image"])
            x1, y1, x2, y2 = map(int, spr["region"].split(" "))
            break
    timg = images[img-1].crop((x1, y1, x2, y2))
    timg.save(f"./item/tmp/{idx}.png")
    img = Img(f"./item/tmp/{idx}.png")
    
    ws.append([item["idx"], item["titlestr"], item["textstr"], item["type"], item["hp"], item["mp"]])
    ws.add_image(img, f"G{idx}")
    rd = ws.row_dimensions[idx] # get dimension for row 3
    rd.height = 25 # value in points, there is no "auto"
    idx += 1
wb.save(save_path)
