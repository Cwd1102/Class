"""
File:    diff.py
Author:  Ouwen Dai
Date:    9/27/22
Section: 56
E-mail:  odai1@umbc.edu
Description: Takes user inputted list and finds the biggest difference between values

"""

def main():

    #stores user input for the amount of data sets they want
    num_list = int(input("How many items do you wish to enter into the list?"))

    #stores the list for the user inputted values
    int_list = list()

    #stores the highest differnce between values in the list
    highest_num = 0

    #asks the user to input a user set series of floats
    for i in range(num_list):
        print("Please enter value", i + 1 , "into the data list")
        num = float(input(""))
        int_list.append(num)
    
    #checks every pair of numbers in list to see difference between values
    #for loop subtracts list length to prevent i from being outside of list
    for i in range(len(int_list) - 1):
        compare = int_list[i + 1] - int_list[i]
        if(compare < 0):
            compare = compare * -1

        if(compare > highest_num):
            highest_num = compare
    print(highest_num)

main()