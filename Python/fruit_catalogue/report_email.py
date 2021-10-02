#!/usr/bin/env python3

import os, datetime
import emails
from reports import generate_report
from icecream import ic

#Get the currrent date
current_date = datetime.datetime.now().strftime('%Y-%m-%d')

def generate_pdf(path):
    pdf = ""
    files = os.listdir(path)
    for file in files:
        if file.endswith(".txt."):
            with open(path + file, 'r') as f:
                lines = f.readlines()
                name = lines[0].strip()
                weight = lines[1].strip()
                pdf += "name: " + name + "<br/>" + "weight: " + weight + "<br/><br/>"
    return pdf


def main():
    path = "supplier-data/descriptions/"
    title = "Process Updated on " + current_date
    #Generate pdf body
    additional_info = generate_pdf(path)
    generate_report("/tmp/processed.pdf", title, additional_info)

    #Email data
    sender = "automation@example.com"
    receiver = "{}@example.com".format(os.environ["USER"])
    subject = "Upload Completed - Online Fruit Store"
    body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
    attachment = "/tmp/processed.pdf"

    #Generate and send email
    message = emails.generate_email(sender,receiver,subject,body,attachment)
    emails.send_email(message)
if __name__ == '__main__':
    main()