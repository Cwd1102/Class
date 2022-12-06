"""
File: filesystem.py
Author: Ouwen Dai   
Date: 11/29
Lab Section: 56
Email:  odai1@umbc.edu
Description : simulates basic commands of a file system controlled via terminal
"""
#TODO: debug
#* Completed: ls , pwd , helper functions , cd , locate , rm , touch , mkdir
"""
* turns the directory path into a list
* param current_directory: path of the directory
* return : a list of the path to the current directory
"""
def dictionary_path_list(current_directory):
    # returns directory if it already a list

    if (type(current_directory) == type([])):
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
    if ((user_input[0] == "/") and (user_input[-1] == "/")) or (user_input[0] == "ls"):
    #gets all the names of the keys
        items = current_file.keys()
        for name in items:
            #if the key is a file
            if name == 'files':
                for txt in (current_file[name]):
                    print(txt)
            else:
                print(name)
    else:
        print("invalid format")

#user_command: what the user inputs into terminal
#Ex: 'cd dir'
#return: list , ['cd'] , ['dir]
def input_split(user_command):
    #returns exit to prevent loop
    if user_command.strip() == "exit":
        return "exit"
    
    if " " not in user_command:
        return [user_command]

    #splits string if there is a space in string
    if " " in user_command.strip():
        command_list = user_command.split()
    space_count = 0
    list = []

    for i in range(len(user_command)):
        if user_command[i] == " ":
            space_count = 1
        if space_count == 1 : 
            list.append(user_command[0: i: 1])
            if i + 1 != len(user_command) :
                list.append(user_command[i + 1: len(user_command): 1])
            else:
                list.append(user_command[i: len(user_command): 1])
                return list
"""
* checks if the file path exists
* param main_file: main dictionary
* param file_path = filepath of the desired file/directory
* returns True if path exists and False if it dosent
"""
def path_check(main_file , file_path):
    if file_path != "/":
        if file_path[0] == "/":
            file_path = file_path[1 : ]
        if file_path[-1] == "/":
            file_path = file_path[ : -1]
    else:
        return True

    if type(file_path) != type([]):
        file_path = file_path.split("/")
    keys = list(main_file.keys())

    #if the directory/file exists in the current directory
    if file_path[-1] in keys:
        return True
    
    #moves to the next directory if it exists, otherwise return false
    for name in keys:
        if file_path[0] == name:
            new_file = main_file[name]
            return path_check(new_file , file_path[1 :])
    return False

"""
*moves the current working directory to the specified user input
*param user_input: command that the user inputted type(list)
*param current_file: dictionary open to the current working directory
*param current_directory: filepath of the current directory
*param main_file: dictionary of the main file system
"""
def cd(user_input , current_file , current_directory , main_file):
    # removes the cd command from list
    user_input = user_input[1]
    #turns the current directory into a list
    current_directory_list = dictionary_path_list(current_directory)

    if current_directory == user_input:
        return current_directory
    
    #runs if user inputs ".."
    if user_input == "..":
        #runs if user inputs "/"
        if current_directory == "/": #!failsafe
            print('already in root directory')
            return "/"
        
        #runs if user input is not "/"
        else:
            #removes right most path from directory_path
            prev_directory = "/".join(current_directory_list[ : -1])
            #runs if user hits root directory
            if len(prev_directory) == 0:
                return "/"
            return (f"/{prev_directory}/")
    
    #! failsafe
    #checks if user input has any missing "/"s             
    if path_check(main_file , current_directory + user_input):
            
            #if the first index of string is "/"
            if user_input[0] == "/":
                return user_input
            
            # if last index of string is "/"
            if user_input[-1] != "/":
                user_input = user_input + "/"
            
            #if the user is trying go to the current directory
            if "/" + user_input == "/" + current_directory_list[-1] + "/":
                print("already in current directory")
                return "/" + user_input
            return current_directory + user_input
    else:
        print("path does not exist")
        return current_directory

"""
*locates all instances of a .txt file
*param user_input: command that the user inputted type
*param file_system: current directory
*param current_directory: filepath of the current directory
*param path: list
*returns all paths for .txt file
"""
def locate(user_input ,file_system , current_directory , path):
    current_directory_list = dictionary_path_list(current_directory)   
    var = user_input[-4 : ]
    
    #checks if file is text file
    if user_input[-4 :] != ".txt":
        print("please input valid file")
    else:
        keys = list(file_system.keys())
        files = 0
        
        #if there is nothing in directory
        if len(keys) == 0:
            return path

        #if directory has files
        if 'files' in keys:
            files = 1

        #list of paths of found file
        if user_input in file_system['files']:
            path.append(current_directory.strip() + user_input + "/")
        
        #looks into deeper file paths (recursive)
        for name in keys:
            if name != 'files':    
                temp_file_system = file_system[name]
                temp_directory = (f"{current_directory}{name}/")

                locate(user_input, temp_file_system , temp_directory , path)
        return path
"""
*makes new directory in current directory
*param main_file: main file system
*param userinput: name of the new directory 
*param current_directory: path for the current directory
*param current_file_system: directory of the current path
*return dictonary with new directory 
"""
def mkdir(main_file , user_input , current_directory ,  current_file_system):
    main_file_copy = main_file
    current_directory_list = dictionary_path_list(current_directory)
    keys = list(main_file.keys())

    if main_file == current_file_system:
        main_file_copy[user_input] = {}
        return main_file_copy
    
    for names in keys:
        if names != "files":
            temp_file_system = main_file_copy[names]

            mkdir(temp_file_system , user_input , current_directory , current_file_system)
    return main_file_copy

"""
*removes text file in current directory
*param main_file: main file system
*param userinput: name of the new directory 
*param current_directory: path for the current directory
*param current_file_system: directory of the current path
*return dictonary with inputted text file removed
"""
def rm(main_file , user_input , current_directory ,  current_file_system):
    main_file_copy = main_file
    current_directory_list = dictionary_path_list(current_directory)
    keys = list(main_file.keys())

    if main_file == current_file_system:
        temp_file_system = main_file_copy["files"]
        for i in range(len(main_file_copy["files"])):
                if temp_file_system[i] == user_input:
                    temp_file_system.pop(i)    
        return main_file_copy    
    for name in keys:
        if name != "files":
            rm(main_file_copy[name] , user_input , current_directory , current_file_system)    
    return main_file_copy

"""
*creates text file in current directory
*param main_file: main file system
*param userinput: name of the new directory 
*param current_directory: path for the current directory
*param current_file_system: directory of the current path
*return dictonary with inputted text file added
"""
def touch(main_file , user_input , current_directory ,  current_file_system):
    main_file_copy = main_file
    current_directory_list = dictionary_path_list(current_directory)
    keys = list(main_file.keys())

    if main_file == current_file_system:
        main_file_copy["files"].append(user_input)
        return main_file_copy
    
    for names in keys:
        if names != "files":
            temp_file_system = main_file_copy[names]

            touch(temp_file_system , user_input , current_directory , current_file_system)
    return main_file_copy

#main terminal program
def main_term():
    condition = ""
    file_key = 'files'
    directories_key = "directories"
    #variable for the current directory
    current_directory = "/"

    """
    *File System
    /
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
                file_key : ['random.txt' , 'random_1.txt' , 'random_2.txt' , 'inception.txt']
            },
            'home_2' : {
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
        if condition[0] == "pwd":
            print(current_directory)

        #! user input: ls    
        if (condition[0] == "ls") or condition == "ls":
            print("contents for" , current_directory)
            if len(condition) == 2:
                temp_file_system = cwd(condition[1] , my_file_system)
                ls(condition[1] , temp_file_system)
            else:    
                ls(condition , current_file_system)
        
        #! user input: cd
        if (condition[0] == "cd") and (type(condition) == type([])):
            current_directory = cd(condition , current_file_system , current_directory ,  my_file_system)

        #! user input: locate
        if (condition[0] == "locate"):
            path = []
            path = locate(condition[1] , current_file_system , current_directory , path)
            if len(path) == 0:
                print("file not found")
            else:
                print("A file with that name was found at the following paths")               
                for i in range(len(path)):
                    print(path[i])

        #! user input: mkdir
        if (condition[0] == "mkdir"):
            my_file_system = mkdir(my_file_system, condition[1] , current_directory , current_file_system)

        #! user input: rm
        if (condition[0] == "rm"):
            my_file_system = rm(my_file_system, condition[1] , current_directory , current_file_system)

        #! user input: touch
        if(condition[0] == "touch"):
            my_file_system = touch(my_file_system, condition[1] , current_directory , current_file_system)


if __name__ == '__main__':
    #main call
    main_term()