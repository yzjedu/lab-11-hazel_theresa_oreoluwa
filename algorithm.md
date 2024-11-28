# Algorithm Document

High Level Tasks
1. error check user input file name
2. read file to list 
3. morse code conversion information
4. read the morse code text 
5. converting morse code to english and writing to new file 
6. main 


Function 1 :
name: read_file_name
parameters: none
return: file name
Algorithm:
1. Prompt the user to enter a file name
2. While the file name does not exist:
   1. Prompt the user to enter a file name again
3. return filename


Function 2:
name: read_file_to_list
parameters: filename
return:list
Algorithm: 
1. create an empty list, and store as list
2. open filename and store as input_file
3. for each line in input_file:
   4. strip line of white space
   5. append line to list
4. return list

Function 3
name: morse_code_dictionary
parameters: list
return: dictionary
Algorithm:
1. Prompt user to enter translation file
2. set dictionary as an empty dictionary
3. call read_file_name of user input
4. Open file for reading and store as input_file
2. For line in input_file:
   3. split the line, and store as input_list
   4. if the length of input_list is equal to 2
      5. dictionary[itemlist[1]] equals itemlist[0]
6. return dictionary


Function 4 
name:converting_to_english
parameters: dictionary and user_list
return: none
Algorithm: 
1. For line in user_list:
   2. split line by "   " and store as words 
   3. for each word in words:
      4. set an empty string as decoded word
      5. for each item in word:
         6. if item in dictionary
         7. Set translated word to equal dictionary[item]
      8. append translated word to a line
   9. append line to list
   10. return list.
         

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
6. call converting_to_english and store as user_list
7. call write_user_list_to_file using user_list 
8. output success and thanks message


call main()










