#! /usr/bin/env python3

from icecream import ic
import requests
import glob

url = "http://localhost/upload/"
path = "C:/Users/Raza/Desktop/Python/images/"

def upload_image(filepath):
    with open(filepath) as opened:
        response = requests.post(url, files={'file': opened})
        response.raise_for_status()


def main():
    for file in glob.glob("{}*jpeg".format(path)):
        ic(file)
        #upload_image(file)

if __name__ == '__main__':
    main()