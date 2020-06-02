#!python3

"""
v1.0
Author - Nirmalya Nayak
Python 3.7.6
OS - Windows 10 Home Single Language (1809) #I Know Its Outdated ;).
A Very Simple Renaming Script Which Takes Target Folder as Input and Batch Rename Files.
"""

#Import OS & Regex Module.
import os, re

#Not Necessary. But, Hey What The Heck.
print("Current Directory:", os.getcwd())

#Takes The Folder Name From The Use As Input.
print("Type Absolute Paht of The Folder: ")
path = input()
print(path)
#E:\MOOC\PROGRAMMING\Web Development\JavaScript

#Changes The Active Directory To User Given Folder/Directory.
os.chdir(path)
print("Current Directory:", os.getcwd())

#Gets All The File Names As List And Stores It To The Variable.
all_items_in_folder = os.listdir(path)
#[print(type(_)) for _ in all_items_in_folder]

#Using Try-Catch Block To Make Program Fail Safe.
try:
    #Code
    #pattern = re.compile(r"\d+[/]\d+") --- Didn't Work Because The OS Module Doesn't Consider Special Characters.
    pattern = re.compile(r"\d+")	   #--- Using RE Module, It Looks For Digits("+" Symbol Checks For 1 or More).
    for _ in all_items_in_folder:
        if len(pattern.findall(_)[0]) == 1:
            renamed_file = "0" + pattern.findall(_)[0] + " " + _
        else:
            renamed_file = pattern.findall(_)[0] + " " + _
        print(renamed_file)
        os.rename(_, renamed_file)
    
except OSError:
    #If Fails.(Which Is Inevitable. Ha Ha Ha)
    print("Renaming Failed.")
finally:
    print("Peace")