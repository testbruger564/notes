#!/usr/bin/env python3

import os
from os import path
import os.path

print ("Welcome to notes")

# Saves the current location in a variable named current_directory.

current_directory = os.getcwd()


folder = input("Insert folder name: ")
filepath = "{}/{}".format(current_directory, folder)

try:

    # Creates the folder.

    os.mkdir(filepath)
    print("Directory '{}' is created.".format(folder))

    # Creates the file.

    file = input("Insert file name: ")

    path = "%s/%s" % (filepath, file)

    print ("File '{}' is created.".format(file))
    os.system("$EDITOR " + path)

    print (path)

except FileExistsError:
    print("The directory '{}' does already exist.".format(folder))

    file = input("Insert file name: ")

    path = "%s/%s" % (filepath, file)


    # Checks if the file exists
    # If it does exist, it get opened
    # if it doesn't exist, it gets created and opened.

    if os.path.isfile(path):
        print ("File exist")
        os.system("$EDITOR " + path)
    else:
        print ("File not exist")
        os.system("$EDITOR " + path)

    print (path)