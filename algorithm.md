# Algorithm Document

#### THINK before you code...
#### Write down the list of tasks to help you think


High Level Tasks
1. error check user input file name
2. read file to list 
3. morse code conversion information
3. read the morse code text 
4. converting morse code to english and writing to new file 
5. main 


Function 1 :
name: read_file_name
parameters: none
return: file name
Algorithm:
1. prompt user to enter a file name
2. while file name does not exist:
   3. prompt user to enter a file name
4. return filename


Function 2:
name: read_file_to_list
parameters: filename
return:list
Algorithm: 
1. create an empty list, and store as list
2. open filename and store as input file
3. read lines from input file to list
4. return list

Function 3
name: morse_code_dictionary
parameters: list
return: dictionary
Algorithm:
1. set dictionary as an empty dictionary
2. For line in list:
   3. split the line, and store as itemlist
   4. split itemlist 
   5. morse_dictionary[itemlist[2]] equals itemlist[1]
6. return dictionary


Function 4 
name:converting_and_writing_to_english
parameters: dictionary and user_list
return: none
Algorithm: 
1. For line in user_list:
   2. split line by space
3. For item in user_list:
   4. item equals dictionary[item]
5. return user_list


Function 5
name:write_user_list_to_file
parameters: user_list
return:none
Algorithm:
1. ask for name of file from user
2. open file for writing
3. For line in user_list:
   4. write to file 
5. close file


Function 6 
name: main 
parameters:none
return: none
Algorithm:
1. output welcome message
2. call read_file_name and store as user_file
3. call read_file_to_list using user_file and store as user_list
4. call read_file_to_list using morsecode.txt and store as morse_code_list
5. call morse_code_dictionary using morse code list and store morse_code_dictionary
6. call converting_and_writing_to_english and store as user_list
7. call write_user_list_to_file using user_list 
8. output success and thanks message


call main()









