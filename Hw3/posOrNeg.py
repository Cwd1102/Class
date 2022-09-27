"""
File:    psotORNeg.py
Author:  Ouwen Dai
Date:    9/27/22
Section: 56
E-mail:  odai1@umbc.edu
Description: Adds integers to a list based on the user's predetrmined length and value
then determines if each number in the list is positive, negative, or unassigned

"""
def main():
    num_list = int(input("How many items do you wish to enter into the list?"))
    
    data_list = list()

    for i in range(num_list):
        print("Please enter value #",i + 1 , "into the data list:")
        num = int(input(""))
        data_list.append(num)
    
    for i in range(len(data_list)):
        if(data_list[i] == 0):
            print("Value #",i + 1 , data_list[i] , "is unassigned") 
        elif(data_list[i] > 0):
            print("Value #",i + 1 , data_list[i] , "is Positive")
        elif(data_list[i] < 0):
            print("Value #",i + 1 , data_list[i] , "is Negative")
main()