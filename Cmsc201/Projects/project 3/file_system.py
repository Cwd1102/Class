"""
File: filesystem.py
Author: Ouwen Dai   
Date: 11/29
Lab Section: 56
Email:  odai1@umbc.edu
Description:
"""
#variable for the current directory
current_directory = "/"


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


def main_term():
    condition = ""

    while(condition != "exit"):
        
        #main terminal for user to input commands
        condition = input_split(input("[cmsc201 proj3]$ ").lower())
        #condition == type(list)
        

        #prints current working directory 
        if condition[0] == "pwd":
            print(current_directory)
        
        #moves current working directory to user specified path
        if condition[0] == "cd":
        
            cd(condition[1])


if __name__ == '__main__':

    directory = "directories"
    file = "files"
    
    my_file_system = {
        'home' : {
            
        }
    }
    main_term()