"""
File:    freq.py
Author:  Ouwen Dai
Date:    9/27/22
Section: 56
E-mail:  odai1@umbc.edu
Description: Takes user inputted list and finds # of values in the list requested by user

"""
def main():  

    #stores the list
    num_list = list()
    
    #loops for 6 times
    #every loop adds one user inputted integer into list
    for i in range(6):
        print("please enter value #",i + 1 ,"into the data list")
        num_list.append(int(input("")))
    
    #stores the number the user would like to check the frequence of in the list
    user_num = int(input("Please enter a number to check the frequency:"))

    num_val = 0

    #loops for the length of num_list times
    #adds 1 to num_val every time loop finds number in list corresponding with user_num
    for i in range(len(num_list)):
        if(user_num == num_list[i]):
            num_val += 1
    print("We found" , num_val , "value(s) of"  , user_num , "within the data list given")
    


main()