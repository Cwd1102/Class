"""
File:    highest.py
Author:  Ouwen Dai
Date:    9/27/22
Section: 56
E-mail:  odai1@umbc.edu
Description: takes the user's inputted integers and finds the highest values

"""

def main():
    
    list_leng = int(input("How many items do you wish to enter into the list?"))
    
    list_num = list()

    highest_num = 0
    
    for i in range(list_leng):
        print("Please enter value#",i + 1 , "into the data list:")
        x = int(input(""))
        list_num.append(x)

    for i in range(len(list_num)):
        if(list_num[i] > highest_num):
            highest_num = list_num[i]
    print("The highest value is" , highest_num)

main()