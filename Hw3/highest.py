"""
File:    highest.py
Author:  Ouwen Dai
Date:    9/27/22
Section: 56
E-mail:  odai1@umbc.edu
Description: takes the user's inputted integers and finds the highest values

"""

def main():
    
    #stores how many series of data the user wants in ther list
    list_leng = int(input("How many items do you wish to enter into the list?"))
    
    #stores the list
    list_num = list()

    #stores the number for the highest value in the list
    highest_num = 0
    
    #loops for list_leng time
    #appends user inputted integer into list
    for i in range(list_leng):
        print("Please enter value#",i + 1 , "into the data list:")
        x = int(input(""))
        list_num.append(x)

    #loops for length of list times
    #overrights highest_sum evertime there is a number higher than number in highest_sum
    for i in range(len(list_num)):
        if(list_num[i] > highest_num):
            highest_num = list_num[i]
    print("The highest value is" , highest_num)

main()