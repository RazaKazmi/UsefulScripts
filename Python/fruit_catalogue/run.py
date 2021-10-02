#! /usr/bin/env python3

from icecream import ic
import os
import requests

url = "http://yoururl/fruits"
description_path = "C:/Users/Raza/Desktop/Python/images/"
text_files = os.listdir(description_path)

def upload_fruit_data(filepath):
    fruit_data = {}
    ic(filepath)
    filename = os.path.basename(filepath)
    ic(filename)
    #Open description file and read data into dictionary
    with open(filepath, 'r') as file:
        lines = file.readlines()
        fruit_data["name"] = lines[0].strip()
        # remove 'lbs' from the weight
        weight = lines[1].strip()
        weight = weight[:-4]
        fruit_data["weight"] = int(weight)
        fruit_data["description"] = lines[2].strip()
        fruit_data["image_name"] = filename.replace(".txt",".jpeg")
    ic(fruit_data)
    send_to_webservice(fruit_data)

def send_to_webservice(dict_data):
    #Send our Post request to our URL in JSON format
    response = requests.post(url, json=dict_data)
    #Raise exception is there is a status code error
    response.raise_for_status()

    status_code = response.status_code
    print("Data sent. Response code: {}".format(status_code))

def main():
    for file in text_files:
        upload_fruit_data(description_path + file)

if __name__ == '__main__':
    main()