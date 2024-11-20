# Programmers:
# Course:  CS151, Dr. Zelalem Jembre Yalew
# Due Date:
# Lab Assignment: 11
# Problem Statement:
# Data In:
# Data Out:


import os

#Purpose: error check user input file name
#Parameter: none
#Return: file_name
def read_file_name():
    file_name = input("Please enter the file name you would like to translate: ")
    while not os.path.isfile(file_name):
        print("File does not Exist.")
        file_name = input("Please enter a valid file name you would like to translate: ")
    return file_name

#Purpose: Read a file to a list
#Parameter: file_name
#Return: list
def read_file_to_list(file_name):
    list = []
    with open(file_name, 'r') as input_file:
        list = input_file.readlines()
    return list