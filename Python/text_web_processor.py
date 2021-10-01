#!/usr/bin/env python3

# A python script to process text files for user feedback and send it to a web service
# The txt files must be in the format:
#title
#name
#date
#feedback/description 

import os
import requests

url = "http://yoururl/feedback/"
path = "/data/feedback/"
files = os.listdir(path)

def parse_feedback(txt_file):
    feedback_dict = {}
    #Open file and read data into dictionary
    with open(txt_file, 'r') as file:
        lines = file.readlines()
        feedback_dict["title"] = lines[0].strip()
        feedback_dict["name"] = lines[1].strip()
        feedback_dict["date"] = lines[2].strip()
        feedback_dict["feedback"] = lines[3].strip()
    #send our dictionary data to webservice    
    send_to_webservice(feedback_dict)
    

def send_to_webservice(dict_data):
    #Send our Post request to our URL in JSON format
    response = requests.post(url, json=dict_data)
    #Raise exception if there is a status code error
    response.raise_for_status()

    status_code = response.status_code
    print("Data sent. Response code: {}".format(status_code))


def main():
    for file in files:
        parse_feedback(os.path.join(path,file))

if __name__ == '__main__':
    main()