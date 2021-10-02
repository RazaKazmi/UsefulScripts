#! /usr/bin/env python3

import sys
import os
import glob
from PIL import Image
from icecream import ic


size = 600, 400
img_format = ".jpeg"
img_path = "C:/Users/Raza/Desktop/Python/images/"


def process_image(file):
    filepath, ext = os.path.splitext(file)
    ic(filepath)
    with Image.open(file) as img:
        img = img.resize(size)
        img.convert("RGB").save(filepath + img_format, format='JPEG')

def main():
    files = os.listdir(img_path)
    for file in files:
        ic(file)
        if not file.startswith('.'):
            process_image(img_path + file)


if __name__ == '__main__':
    main()