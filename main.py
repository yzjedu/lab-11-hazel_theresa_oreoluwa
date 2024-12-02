# Programmers: Oreoluwa Adebusoye, Hazel Osborne , Theresa DeJacimo
# Course:  CS151, Dr. Zelalem Jembre Yalew
# Due Date: 11/28/24
# Lab Assignment: 11
# Problem Statement: Converting a program from morse code back to english
# Data In: Morse code translation file, input file
# Data Out: Decoded output file


import os

#Purpose: Error check user input file name
#Parameter: none
#Return: file_name
def read_file_name(prompt_message):
    file_name = input(prompt_message)
    while not os.path.isfile(file_name):
        print("File does not Exist.")
        file_name = input(prompt_message)
    return file_name


#Purpose: Read a file to a list
#Parameter: file_name
#Return: list
def read_file_to_list(file_name):
    list = []
    with open(file_name, 'r') as file:
        for line in file:
            line = line.strip()
            list.append(line)
    return list

#Purpose: Create list into dictionary
#Parameters: list
#Return: dictionary
def morse_code_dictionary():
    print("\nProvide the Morse code translation file (e.g., morsecode.txt).")
    morse_file = read_file_name("Enter the name of the Morse code translation file: ") # Validate file input
    print("_" * 75)

    dictionary = {}

    with open(morse_file, 'r') as input_file:
        for line in input_file:
            input_list = line.strip().split()
            if len(input_list) == 2: # Ensure the line is valid
                dictionary[input_list[1]] = input_list[0]
    return dictionary

#Purpose: Converting morse code to english
#Parameters: dictionary and user_list
#Return: user_list
def converting_to_english(dictionary,user_list):
    decoded_list = []
    for line in user_list:
        words = line.split("   ")    # Words are separated by three spaces
        translated_line = []
        for word in words:
            translated_word = ""
            for code in word.split():  # Letters are separated by one space
                if code in dictionary:
                    translated_word += dictionary[code]
            translated_line.append(translated_word)
        translated_string = ""
        for word in translated_line:
            translated_string += " "
            translated_string += word
        decoded_list.append(translated_string.strip())
    return decoded_list


# Purpose: Writes the decoded English text to a file
# Parameter: list of decoded words
# Return: None
def write_list_to_file(user_list):
    output_file = input("Enter the name of the output file: ")
    with open(output_file, 'w') as file:
        for line in user_list:
            file.write(line + '\n')  # Write each line followed by a newline
    print(f"Decoded content has been written to '{output_file}'.")
    print("_" *75)


# Purpose: Coordinates the program flow
# Parameter: None
# Return: None
def main():
    # Output a welcome message
    print("_" *75)
    print("Welcome to the Morse Code Decoder!")
    # Get the input file name from the user
    print("_" *75)
    input_file = read_file_name("Please enter a valid file name you would like to translate: ")
    #  Read the input file into a list
    user_list = read_file_to_list(input_file)
    # Check the Morse code file
    # Read into a list into Morse Code Dictionary
    morse_dict = morse_code_dictionary()
    # Convert the Morse code in user_list to English
    english_list = converting_to_english(morse_dict, user_list)
    # Write the decoded English text to an output file
    write_list_to_file(english_list)
    print("Decoding complete! Thank you for using the Morse Code Decoder.")

main()





