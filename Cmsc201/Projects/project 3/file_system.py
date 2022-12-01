"""
File: filesystem.py
Author: Ouwen Dai   
Date: 11/29
Lab Section: 56
Email:  odai1@umbc.edu
Description:
"""

def dictionary_path_list(current_directory):
    if type(current_directory) == type([]):
        return current_directory
    if current_directory == '/':
        return '/'
    
    if "/" not in current_directory:
        current_list = [current_directory]       
        return current_list  
    
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

def ls(user_input , current_file):
    current_directory_list = dictionary_path_list(user_input)

    if len(current_directory_list) == 1:
        items = current_file.keys()
        for name in items:
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
    
    #splits string if there is a space in string
    if " " in user_command.strip():
        command_list = user_command.split()
        return command_list
    return user_command


#main terminal program
def main_term():
    condition = ""
    file_key = 'files'
    directories_key = "directories"
    #variable for the current directory
    current_directory = "/home/home_1/"

    my_file_system = {
        'home' : {

            'home_1' : {
                'home_1_1' : {} , 'home_1_2' : {},
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
        #prints current working directory 
        if condition == "pwd":
            print(current_directory)
        
        if (condition[0] == "ls") or condition == "ls":
            ls(condition[1] , current_file_system)
        
        #moves current working directory to user specified path
        if condition[0] == "cd":
            current_directory = cd()


if __name__ == '__main__':
    main_term()