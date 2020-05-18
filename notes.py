#!/usr/bin/env python3

import os
from os import path
import os.path

print ("Welcome to notes")

# Saves the current location in a variable named current_directory.

current_directory = os.getcwd()


folder = input("Insert folder name: ")
filesti = "{}/{}".format(current_directory, folder)

try:

    # Creates the folder.

    os.mkdir(filesti)
    print("Directory '{}' is created.".format(folder))

    # Creates the file.

    file = input("Insert file name: ")

    sti = "%s/%s" % (filesti, file)

    print ("File '{}' is created.".format(file))
    os.system("subl " + sti)

    print (sti)

except FileExistsError:
    print("The directory '{}' does already exist.".format(folder))

    file = input("Insert file name: ")

    sti = "%s/%s" % (filesti, file)


    # Checks if the file exists
    # If it does exist, it get opened
    # if it doesn't exist, it gets created and opened.

    if os.path.isfile(sti):
        print ("File exist")
        os.system("subl " + sti)
    else:
        print ("File not exist")
        os.system("subl " + sti)

    print (sti)