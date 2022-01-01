#!/usr/bin/python

#Program will brute force password protected zip files (Numbers/Codes ONLY)
#To make a zip file to test the program on, you can use the following command:
#zip -re zip_file_to_make.zip dir_with_secret_files

from zipfile import ZipFile
import sys

try:
    name = sys.argv[1]
except:
    print("-"*60)
    print("Error: Program needs 1 argument (Target Zip File)")
    print("-"*60)
    exit()

zip_file = ZipFile(name)

for i in range(10000):
    try:
        zip_file.extractall(pwd=str(i))
        print("PASSWORD: {}".format(str(i)))
        break
    except:
        pass


