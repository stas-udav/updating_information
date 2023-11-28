#!/usr/bin/env python3
import requests
import os

# This example shows how a file can be uploaded using
# The Python Requests module

# url = "http://localhost/upload/"
# with open('/usr/share/apache2/icons/icon.sheet.png', 'rb') as opened:
#     r = requests.post(url, files={'file': opened})

url = "http://localhost/upload/"

for file in os.listdir("~/supplier-data/images"): #Iterating through Files in the folder/directory
    if file.endswith(".jpeg"): # Iterate through JPEG files only
        with open(os.path.join("~/supplier-data/images", file), "rb") as opened: #opening jpeg files
            r = requests.post(url, files={"file": opened}) # sending jpeg files on server
            if r.status_code == 200: 
                print(success)
            else:
                print(f" {file} error")