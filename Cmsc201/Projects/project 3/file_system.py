"""
File: filesystem.py
Author: Ouwen Dai   
Date: 11/29
Lab Section: 56
Email:  odai1@umbc.edu
Description:
"""
#TODO: cd(in progress), locate, mkdir, rm, touch, debug
#Completed: ls , pwd , helper functions
"""
* turns the directory path into a list
* param current_directory: path of the directory
* return : a list of the path to the current directory
"""
def dictionary_path_list(current_directory):
    # returns directory if it already a list
    if type(current_directory) == type([]):
        return current_directory    #! Failsafe
    
    # returns directory if it is in root directory
    if current_directory == '/':
        return '/'  #! Failsafe
    
    # if path is only one jump forward
    if "/" not in current_directory:
        current_list = [current_directory]       
        return current_list  

    # splits user inputted path into list
    # splits on every instance of "/"
    current_directory = current_directory[1 : len(current_directory) - 1].split("/")
    return current_directory

#changes the current working directory
def cwd(current_directory , directory):
    #turns path into a list
    current_directory_list = dictionary_path_list(current_directory)
    
    #if the directory is root
    if current_directory == "/":
        return directory

    #checks if last index of path is in the key of directory
    if current_directory_list[-1] in directory.keys():
        new_directory = directory[current_directory_list[-1]]
        return new_directory
   
    #checks if first index of list is in the key of directory
    if current_directory_list[0] in directory.keys():
        new_directory = directory[current_directory_list[0]]
        return cwd(current_directory_list[1 : ] , new_directory)

"""
* prints out all files and directories in stated file
* param user input: path to the file EX: [/home/]
* param current_file: current working directory
"""
def ls(user_input , current_file):
    #calls dictionary_path_list() 
    current_directory_list = dictionary_path_list(user_input)
    #finds all keys of the current directory
    items = current_file.keys()

    #gets all the names of the keys
    for name in items:
        #if the key is a file
        if name == 'files':
            for txt in (current_file[name]):
                print(txt)
        else:
            print(name)

#user_command: what the user inputs into terminal
#Ex: 'cd dir'
#return: list , ['cd'] , ['dir]
def input_split(user_command):
    
    #returns exit to prevent loop
    if user_command.strip() == "exit":
        return "exit"
    
    if user_command == '':
        return ['']

    #splits string if there is a space in string
    if " " in user_command.strip():
        command_list = user_command.split()
        return command_list
    
    return user_command
"""
* checks if the file path exists
* param main_file: main dictionary
* param file_path = filepath of the desired file/directory
* returns True if path exists and False if it dosent
"""
def path_check(main_file , file_path):
    path_list = dictionary_path_list(file_path)
    keys = list(main_file.keys())

    #if the directory/file exists in the current directory
    if path_list[-1] in keys:
        return True
    
    #moves to the next directory if it exists, otherwise return false
    for name in keys:
        if path_list[0] == name:
            new_file = main_file[name]
            return path_check(new_file , path_list[1 :])
    return False

def cd(user_input , current_file , current_directory):
    user_input = user_input[1]
    current_directory_list = dictionary_path_list(current_directory)

    if user_input == "..":
        if current_directory == "/":
            print('already in root directory')
            return "/"
        else:
            prev_directory = "/".join(current_directory_list[ : -1])
            return (f"/{prev_directory}/")
            


#main terminal program
def main_term():
    condition = ""
    file_key = 'files'
    directories_key = "directories"
    #variable for the current directory
    current_directory = "/home/home_1/"

    """
    *File System
    home
        home_1
            home_1_1
                test.txt
            home_1_2
            random.txt
            random_1.txt
            random_2.txt
        home_2
            inception.txt
        inside_home.txt
    """
    my_file_system = {
        'home' : {

            'home_1' : {
                'home_1_1' : {file_key : ['test.txt']}, 
                'home_1_2' : {},
                file_key : ['random.txt' , 'random_1.txt' , 'random_2.txt']
            },
            'home_2 ' : {
                file_key : ['inception.txt']
                },

            file_key : ['inside_home.txt']
        
        }
    }
    
    #loop for the terminal
    while(condition != "exit"):
    
        #main terminal for user to input commands
        condition = input_split(input("[cmsc201 proj3]$ ").lower())
        #condition type(list)
        current_file_system = cwd(current_directory , my_file_system)
        
        #! user input: pwd
        if condition == "pwd":
            print(current_directory)

        #! user input: ls    
        if (condition[0] == "ls") or condition == "ls":
            if type(condition) == type([]):
                temp_file_system = cwd(condition[1] , my_file_system)
                ls(condition[1] , temp_file_system)
            else:    
                ls(condition[1] , current_file_system)
        
        #! user input: cd
        if (condition[0] == "cd") and (type(condition) == type([])):
            current_directory = cd(condition , current_file_system , current_directory)


if __name__ == '__main__':
    #main call
    main_term()