#!/usr/bin/env python3

# ZipFile module
import zipfile

# Open and list
zip = zipfile.ZipFile('Archive.zip', 'r')
# print(zip.namelist())  # Lista conteudo interno do arquivo zip
# print()

# Metadata in the zip file
# for meta in zip.infolist():
#     print(meta)
# print()

# Metadata for a specific file
# info = zip.getinfo('cars.txt')
# print(f"Info cars.txt: {info}")
# print()

# Access to files in zip folder
#print(zip.read('techBrands.txt'))
# # or
# with zip.open('scores.txt') as f:
#      print(f.read())

# Extracting files
#zip.extract('cars.txt')  # extraindo um elemento apenas
#zip.extractall() # extraindo tudo


# Closing file
zip.close()

