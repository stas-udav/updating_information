#!/usr/bin/env python3
import os
import datetime
from reports import generate_report
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os.path

def process_text_data(attachment):
    paragraph = ''
    for filename in os.listdir('supplier-data/descriptions'):
        if filename.endswith('.txt'):
            with open(os.path.join('supplier-data/descriptions', filename), 'r') as file:
                lines = file.readlines()

                fruit_name = lines[0].strip()
                fruit_weight = int(lines[1].strip().split(' ')[0])

                paragraph += 'name: {}\nweight: {} lbs\n\n'.format(fruit_name, fruit_weight)

    generate_report(paragraph, title, attachment)

def generate_email(sender, recipient, subject, body, attachment):
    message = MIMEMultipart()
    message['From'] = sender
    message['To'] = recipient
    message['Subject'] = subject

    message.attach(MIMEText(body, 'plain'))

    with open(attachment, 'rb') as f:
        file_data = f.read()

    attachment_part = MIMEText(file_data, 'base64', 'utf-8')
    attachment_part.add_header('Content-Disposition', 'attachment; filename="processed.pdf"')
    message.attach(attachment_part)

    return message

def send_email(message):
  """Sends the message to the configured SMTP server."""
  mail_server = smtplib.SMTP('localhost')
  mail_server.send_message(message)
  mail_server.quit()

if __name__ == "__main__":
    title = 'Processed Fruit Data'
    attachment = '/tmp/processed.pdf'

    process_text_data(attachment)

    # Send email
    sender = 'automation@example.com'
    recipient = 'username@example.com'  # Replace username with the actual recipient
    subject = 'Upload Completed - Online Fruit Store'
    body = 'All fruits are uploaded to our website successfully. A detailed list is attached to this email.'

    message = generate_email(sender, recipient, subject, body, attachment)
    
    send_email(message)
