import sys
import os
from PIL import Image

in_folder = sys.argv[1]
out_folder = sys.argv[2]
out_format = sys.argv[3]

in_path = os.getcwd() + "\\" + in_folder.lstrip(".").lstrip("\\")
out_path = os.getcwd() + "\\" + out_folder.lstrip(".").lstrip("\\")

if len(sys.argv) > 4:
    if sys.argv[4] == "scan":
        for file in os.listdir(in_path):
            if file.endswith(".jpg"):
                print(in_path + file)
                print(out_path)
else:
    for file in os.listdir(in_path):
        if file.endswith(".jpg"):
            img = Image.open(in_path + file)
            img_fn = file.split(".")[0]
            print(f"converting {file} to {out_format}")
            img.save(out_path + img_fn + "." + out_format, out_format)
