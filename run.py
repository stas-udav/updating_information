#! /usr/bin/env python3

import os
import requests

descriptions_dir = "supplier-data/descriptions" # descriptions txt files path 

for filename in os.listdir(descriptions_dir): 
    if filename.endswith('.txt'): # looking only txt files for our loop
        with open(os.path.join(descriptions_dir, filename), 'r') as file: # creating full path for every txt files in directory exp: c/pytho/+001.txt
            lines = file.readlines() # Reading all lines from the file and returning them as a list(list contains all lines)

            fruit_name = lines[0].strip() #getting file name from 1st line. using strip method to delete all spases befor and after words
            fruit_weight = int(lines[1].strip().split(' ')[0]) #getting fruit weith from 2st line. using strip method to delete all spases befor and after words. using split method separated all words by spase, and after getting 1st word(weith) "[]". int make integer from text
            fruit_description = lines[2].strip()#getting fruit_description from 3st line. using strip method to delete all spases befor and after words
            fruit_image_name = filename.split('.')[0] + '.jpeg' #creating file image name by taken filename, deleting extention(txt) and adding new extension (.jpeg)


        # Creating data dictionary with all fruit data for sending to the Django Fruit website
            data = {
                'name': fruit_name,
                'weight': fruit_weight,
                'description': fruit_description,
                'image_name': fruit_image_name
            }

            response = requests.post("http://[linux-instance-external-IP]/fruits", json=data) #sending all data to the Django Fruit in Json format

            if response.status_code == 200:
                print(f"Successfully uploaded fruit data: {filename}")
            else:
                print(f"Failed to upload fruit data: {response.text}")
