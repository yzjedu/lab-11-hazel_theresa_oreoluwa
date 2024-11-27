# Programmers: Oreoluwa Adebusoye, Hazel, Theresa
# Course:  CS151, Dr. Zelalem Jembre Yalew
# Due Date: 11/28/24
# Lab Assignment: 11
# Problem Statement: Converting a program from morse code back to english
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

#Purpose: Create list into dictionary
#Parameters: list
#Return: dictionary
def morse_code_dictionary(list):
    dictionary = {}
    for line in list:
        item_list = line.split()
        print(item_list)
        dictionary[item_list[2]] = item_list[1]
    return dictionary

#Purpose: Converting morse code to english
#Parameters: dictionary and user_list
#Return: user_list
def converting_to_english(dictionary,user_list):
    for line in user_list:
        split_line = line.split('')
        print(split_line)
    for item in user_list:
        item = dictionary[item]
    return user_list


# Purpose: Writes the decoded English text to a file
# Parameter: list of decoded words
# Return: None
def write_list_to_file(user_list):
    output_file = input("Enter the name of the output file: ")
    with open(output_file, 'w') as file:
        for line in list:
            file.write(line + '\n')  # Write each line followed by a newline
    print(f"Decoded content has been written to '{output_file}'.")

# Purpose: Coordinates the program flow
# Parameter: None
# Return: None
def main():
    # Output a welcome message
    print("Welcome to the Morse Code Decoder!")
    # Get the input file name from the user
    input_file = read_file_name()
    #  Read the input file into a list
    user_list = read_file_to_list(input_file)
    # Read the Morse code file into a list
    morse_code_file = read_file_name()
    morse_code_list = read_file_to_list(morse_code_file)
    # Morse Code Dictionary
    morse_dict = morse_code_dictionary(morse_code_list)
    # Convert the Morse code in user_list to English
    english_list = converting_and_writing_to_english(morse_dict, user_list)
    # Write the decoded English text to an output file
    write_list_to_file(english_list)
    print("Decoding complete! Thank you for using the Morse Code Decoder.")

main()





