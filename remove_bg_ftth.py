from PIL import Image
import os

def remove_white_background(input_path, output_path):
    img = Image.open(input_path).convert("RGBA")
    datas = img.getdata()

    new_data = []
    for item in datas:
        if item[0] > 245 and item[1] > 245 and item[2] > 245:
            new_data.append((255, 255, 255, 0))
        else:
            new_data.append(item)

    img.putdata(new_data)
    img.save(output_path, "PNG")

icons = [
    "assets/img/icon-ftth-netgeo.png",
    "assets/img/icon-ftth-num.png",
    "assets/img/icon-ftth-aps.png",
    "assets/img/icon-ftth-apd.png"
]

for icon in icons:
    if os.path.exists(icon):
        print(f"Processing {icon}...")
        remove_white_background(icon, icon)
    else:
        print(f"File {icon} not found.")
