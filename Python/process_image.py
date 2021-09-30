#!/usr/bin/env python3

#A python script to take images from the current directory and process them to be ready as icons.

#TO DO: Allow arguments for image formats, both input and ouput.
#TO DO: Logging and error handling

import sys
import os
import glob
from PIL import Image

size = 128, 128
img_format = "JPEG"
img_path = sys.argv[1]


def process_image(file):
    filepath, ext = os.path.splitext(file)
    path = img_path + '/' + filepath + '.' + img_format 
    with Image.open(file) as img:
        img = img.rotate(90)
        img = img.resize(size)
        img.save(path,format=img_format)


def main():
    for infile in glob.glob("*.png"):
        process_image(infile)


if __name__ == "__main__":
    main()