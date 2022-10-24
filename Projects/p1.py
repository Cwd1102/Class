"""
File: p1.py
Author: YOUR NAME
Date: THE DATE
Lab Section: YOUR LAB Section
Email:  YOUREMAIL@umbc.edu
Description:  This program shows the layout of code in a Python file, and greets
the user with the name of the programmer
"""

''' ***** LEAVE THE LINES BELOW ALONE ***************
********* LEAVE THE LINES BELOW ALONE ***************
********* LEAVE THE LINES BELOW ALONE *************** '''
debug = False

from dataEntry import fill_roster
from dataEntry import fill_attendance_data

''' ***** LEAVE THE LINES ABOVE ALONE ***************
********* LEAVE THE LINES ABOVE ALONE ***************
********* LEAVE THE LINES ABOVE ALONE *************** '''

def list_students_not_in_class(???):
   """
   Compare the swipe log with the given course roster. Place those students that
   did not show up for class into a list.
   :param ????: 
   :param ????:
   :return: ????
   """

def list_all_times_checking_in_and_out(???):
   """
   Looking at the swiping log, this function will list all in and outs for a
   particular Student. Please note, as coded in the p1.py file given, this
   function was called three times with different student values. 
   :param ????: 
   :param ????:
   :return: ????
   """

def list_all_times_checked_in(???):
   """
   This function returns a list of when all student(s) FIRST swipe in. 
   :param ????: 
   :param ????:
   :return: ????
   """    
    
def list_students_late_to_class(???):
    """
    When given a timestamp string and the swipe log, a list of those records
    of students who swiped in late into the class is produced. This function
    returns a list of when all student(s) FIRST swipe in.
    :param ????: 
    :param ????:
    :return: ????
    """ 

def get_first_student_to_enter(???:
    """
    Simply, this function returns the student that swiped in first. Note,
    the order of the data entered into the swipe log as not the earliest
    student to enter.
    :param ????: 
    :param ????:
    :return: ????
    """ 
    

def printList(???):
    """
    Simply prints the list. The function should not be able to change any
    values of that list passed in.
    :param ????: 
    :param ????:
    :return: ????
    """

''' ***** LEAVE THE LINES BELOW ALONE ***************
********* LEAVE THE LINES BELOW ALONE ***************
********* LEAVE THE LINES BELOW ALONE *************** '''

if __name__ == '__main__':
    # Example, Dr. NIcholas, 9am class    
    
    # load class roster here into a list
    classRoster = fill_roster()

    #figure out which attendance data file to load here
    
    #load data
    attendData = fill_attendance_data()
    
    #use different tests 
    # make sure roster was filled 
    #printList(classRoster)
    # make sure attendance data was loaded
    #printList(attendData)
    
    #list all those missing
    print("****** Students missing in class *************")    
    printList(list_students_not_in_class(classRoster, attendData))
    #list signin/out times for a student
    print("****** List all swipe in and out for a student *******")
    printList(list_all_times_checking_in_and_out("Lupoli, Shawn", attendData))
    print("****** List all swipe in and out for a student *******")
    printList(list_all_times_checking_in_and_out("Allgood, Nick", attendData))
    print("****** List all swipe in and out for a student *******")
    printList(list_all_times_checking_in_and_out("Arsenault, Al", attendData))  
    #display when students first signed in (and in attendance)
    print("****** Check in times for all students who attended***")
    printList(list_all_times_checked_in(attendData))  
    #display all of those students late to class
    print("****** Students that arrived late ********************")
    printList(list_students_late_to_class("09:00:00", attendData))
    #display first student to enter class
    print("******* Get 1st student to enter class ****************")    
    print(get_first_student_to_enter(attendData))
    
''' ***** LEAVE THE LINES ABOVE ALONE ***************
********* LEAVE THE LINES ABOVE ALONE ***************
********* LEAVE THE LINES ABOVE ALONE *************** '''
