#! /usr/bin/env python3
import psutil
import smtplib
from email.mime.text import MIMEText
import time

def send_email(message):
    mail_server = smtplib.SMTP('localhost')
    mail_server.send_message(message)
    mail_server.quit()

def check_system_stats():
    # Check CPU usage
    cpu_usage = psutil.cpu_percent()
    if cpu_usage > 80:
        subject = "CPU usage is over 80%"
        body = "Error - CPU usage is over 80%"
        send_email(generate_email(subject, body))

    # Check disk space
    disk_usage = psutil.disk_usage("/")
    available_disk_space = disk_usage.free
    if available_disk_space / disk_usage.total < 0.2:
        subject = "Available disk space is lower than 20%"
        body = "Error - Available disk space is lower than 20%"
        send_email(generate_email(subject, body))

    # Check memory usage
    available_memory = psutil.virtual_memory().available
    if available_memory < 500 * 1024 * 1024:
        subject = "Available memory is less than 500MB"
        body = "Error - Available memory is less than 500MB"
        send_email(generate_email(subject, body))

    # Check hostname resolution
    try:
        socket.gethostbyname("localhost")
    except socket.gaierror:
        subject = "Hostname 'localhost' cannot be resolved to '127.0.0.1'"
        body = "Error - localhost cannot be resolved to 127.0.0.1"
        send_email(generate_email(subject, body))

def generate_email(subject, body):
    message = MIMEText(body, 'plain')
    message['From'] = 'automation@example.com'
    message['To'] = 'username@example.com'
    message['Subject'] = subject

    return message

if __name__ == "__main__":
    while True:
        check_system_stats()
        #time.sleep(60)
