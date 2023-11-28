#!/usr/bin/env python3
import os
import PIL
from PIL import Image


# def convert_images():
# # open image
#     image_directory = "D:\\QA\\updating_catalog_information" # folder w images
# # Указываем директорию с изображениями
#     # image_directory = "~/supplier-data/images"
#     # Расширяем тильду (~) до домашней директории пользователя
#     # image_directory = os.path.expanduser(image_directory)
# # reciving images from folder
#     file_list = os.listdir(folder_path)
 
source_dir = "~/supplier-data/images" #"D:\\QA\\updating_catalog_information"
destination_dir = source_dir

# Iterate through all files in the source directory
for filename in os.listdir(source_dir):
    if filename.endswith('.TIFF'):
        # Load the image
        image = Image.open(os.path.join(source_dir, filename))

        # Check if the image is RGBA
        if image.mode == 'RGBA':
            # Convert the image to RGB format
            image = image.convert('RGB')

        # Resize the image to 600x400 pixels
        resized_image = image.resize((600, 400), Image.Resampling.BILINEAR)

        # Save the resized image as a JPEG file
        new_filename = os.path.splitext(filename)[0] + '.jpg'
        new_filepath = os.path.join(destination_dir, new_filename)
        resized_image.save(new_filepath, quality=90)
        print(new_filename)
