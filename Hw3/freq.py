"""
File:    freq.py
Author:  Ouwen Dai
Date:    9/27/22
Section: 56
E-mail:  odai1@umbc.edu
Description:

"""
def main():  
    num_list = list()
        
    for i in range(6):
        print("please enter value #",i + 1 ,"into the data list")
        num_list.append(int(input("")))
    user_num = int(input("Please enter a number to check the frequency:"))

    x = 0
    for i in range(len(num_list)):
        if(user_num == num_list[i]):
            x += 1
    print("We found" , x , "value(s) of"  , user_num , "within the data list given")



main()