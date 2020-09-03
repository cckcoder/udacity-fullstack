#!/usr/bin/python
import os

def rename_files():
    """ 1.Get file names from folder"""
    file_list = os.listdir(r"./prank")
    save_path = os.getcwd()
    os.chdir(r"./prank")

    """ 2.For each file, rename filename"""
    table = str.maketrans(dict.fromkeys("0123456789"))
    for file_name in file_list:
        new_filename = str(file_name).translate(table)
        os.rename(file_name, new_filename)
    os.chdir(save_path)


rename_files()
