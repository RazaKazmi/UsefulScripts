#!/usr/bin/env python3

import shutil, psutil
import socket
import emails
import os

def check_localhost():
    """Checks if the hostname can be resolved to 127.0.0.1 . Returns a boolean value"""
    localhost = socket.gethostbyname('localhost')
    return localhost == "127.0.0.1"

def check_disk_usage(disk):
    """Checks if theres enough free space on disk. Returns a boolean value."""
    disk_percent_available = 20
    du = shutil.disk_usage(disk)
    free = du.free / du.total * 100
    return free > disk_percent_available

def check_cpu_usage(cpu_percent):
    """Checks if the usage is less then the cpu_percent. Returns a boolean value."""
    usage = psutil.cpu_percent(1)
    return usage < cpu_percent

def check_memory_usage(mb_available):
    """Checks if there is enough free memory available. Returns a boolean value"""
    mu = psutil.virtual_memory().available
    total = mu / (1024.0 ** 2)
    return total > mb_available

def send_email_warning(subject_error):
    sender = "automation@example.com"
    receiver = "{}@example.com".format(os.environ["USER"])
    subject = subject_error
    body = "Please check your system and resolve the issue as soon as possible."
    message = emails.generate_email(sender, receiver, subject, body)
    emails.send_email(message)

def main():
    if not check_localhost():
        subject = "Error - localhost cannot be resolved to 123.0.0.1"
        send_email_warning(subject)

    if not check_disk_usage('/'):
        subject = "Error - Available disk space is less than 20%"
        send_email_warning(subject)

    if not check_cpu_usage(80):
        subject = "Error - CPU usage is over 80%"
        send_email_warning(subject)

    if not check_memory_usage(500):
        subject = "Error - Available Memory is less than 500MB"
        send_email_warning(subject)
    
if __name__ == '__main__':
    main()