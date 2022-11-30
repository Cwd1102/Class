"""
File: py2.py
Author: Ouwen Dai   
Date: 11/7
Lab Section: 56
Email:  odai1@umbc.edu
Description:  This program shows the layout of code in a Python file, and greets
the user with the name of the programmer
"""

# Comment the line below out if your have the load_dictionary function working!!
# Comment the line below out if your have the load_dictionary function working!!

#from dataEntryP2 import fillAttendanceData

# Comment the line above out if your have the load_dictionary function working!!
# Comment the line above out if your have the load_dictionary function working!!

def print_list(xlist):
    for element in xlist:
        print(element)

def connect_to_data_file(filename):
    # will return connection to data file
    infile = ""

    try:
        #infile = open("data.txt", "r")
        #infile = open("dataAllShow1stClass.txt", "r")
        #infile = open("dataAllShow1stAnd2ndClass.txt", "r")
        infile = open(filename, "r")
    except FileNotFoundError:
        print("file was not found, try again")

    return infile  # connection with the file

def print_dictionary(filename):
    print(list(filename.keys()))

def load_dictionary(data):
    dictionary = {}
    for name in data:
        new = name.strip().split(",")
        names =",".join(new[: 2])
        if names not in dictionary:
            numbers = ",".join(new[ 2:])
            dictionary[names] = [numbers]
        else:
            numbers = ",".join(new[ 2:])
            dictionary[names].append(numbers)
    return dictionary

def display_attendance_data_for_student(name , dictionary):
    check = 0

    for names , data in list(dictionary.items()):
        if name == names:
            print(names , data)
            check = 1

    if check == 0:
        print("No student of this name in the attendance log")

def is_present(name, date, dictionary):
    d_list = ",".join(dictionary[name])
    if date in d_list:
        return True 
    else:
        return False

def list_all_students_checked_in(date, data):
    names = []
    
    for name in data:
        for i in range(len(data[name])):
            if date in data[name][i]:
                names.append(name)
    return names

def print_list(list):
    for name in list:
        print(name)

def print_count(list):
    print(f"There were {len(list)} records for this query")

def list_all_students_checked_in_before(date, time, data):
    names = []
    date = int(date.replace("/", ""))
    time = int(time.replace(":", ""))

    for name in data:
        for i in range(len(data[name])):
            temp_list = data[name][i].split(",")
            data_date = int(temp_list[1].replace("/", ""))
            data_time = int(temp_list[0].replace(":", ""))
            
            if data_date == date:
                if data_time < time:
                    names.append(name)
    return names

def list_students_attendance_count(numbers , data):
    name = []
    
    for names in data:
        if len(data[names]) >= numbers:
            name.append(names)
    return name

def list_of_student_no_show(classes_attended , roster , data):
    classes_attended = 2
    attendance = list_students_attendance_count( classes_attended , data)
    names = []
    for name in roster:
        if name not in attendance:
            names.append(name)
    return names

def get_first_student_to_enter(date, data):
    time = 999999
    first_to_enter = ""

    for names in data:
        for i in range(len(data[names])):
            split_list = data[names][i].split(",")
            if split_list[1].strip() == date:
                time_list = int(split_list[0].replace(":" , ""))
                if time_list < time:
                    time = time_list
                    first_to_enter = names
    return first_to_enter

if __name__ == '__main__':

    infile = connect_to_data_file("dataAllShow1stAnd2ndClass.txt")
    infile_roster = connect_to_data_file("rosters.txt")
    if(infile and infile_roster):
        print("connected to data file...")
    else:
        print("issue with data file... STOP")
        exit(1)

    data = load_dictionary(infile)
    roster_data = load_dictionary(infile_roster)
    # ************************
    # OR MANUALLY!!!
    # ************************

    # just making sure the data collected is good
    print_dictionary(roster_data)

    print("********* Looking up Student Attendance Data ***********")
    display_attendance_data_for_student("Morrison, Simon", data)
    display_attendance_data_for_student("Arsenault, Al", data)

    print("********* Looking to see if Student was present on date ***********")
    print(is_present("Bower, Amy", "11/5/2022", data))
    print(is_present("Bower, Amy", "11/14/2022", data))

    # display when students first signed in
    print("**** Students present on this date ****")
    result = list_all_students_checked_in("11/5/2022", data)
    print_list(result)
    print_count(result)

    print("**** Those present on date & before a time assigned ****")
    result = list_all_students_checked_in_before("11/5/2022", "08:55:04", data)
    print_list(result)
    print_count(result)

    # list the good students that showed up both days
    print("**** Those who attended BOTH classes ****")
    #replace int below for # of days to check for
    classes_attended = 2
    
    result = list_students_attendance_count(classes_attended , data)
    print_list(result)
    print_count(result)
    # list the  students that showed up ONE of the days
    print("**** Those who attended ONE class ****")
    classes_attended = 1
    result = list_students_attendance_count(classes_attended , data)
    print_list(result)
    print_count(result)    

    # list the  students that have not shown up
    print("**** Those who have NOT attended a SINGLE class ****")
    classes_attended = 0
    result = list_of_student_no_show(classes_attended , roster_data , data)
    print_list(result)
    print_count(result) 

    print("**** First student to enter on 11/2/2022 ****")
    print(get_first_student_to_enter("11/2/2022" , data))
    
    print("**** First student to enter on 11/3/2022 ****")
    print(get_first_student_to_enter("11/3/2022" , data))

    print("**** First student to enter on 11/4/2022 ****")
    print(get_first_student_to_enter("11/4/2022" , data))

    print("**** First student to enter on 11/5/2022 ****")
    print(get_first_student_to_enter("11/5/2022" , data))