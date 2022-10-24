"""
File:    sos.py
Author:  Ouwen Dai
Date:    10/1/22
Section: 56
E-mail:  odai1@umbc.edu
Description: finds the sum of squares of int input by user

"""

if __name__ == '__main__':

  condition = True 

  while(condition):

    #stores value for the number the user wishes to find the sos
    sos = int(input("What number should we determine the S.O.S.?"))

    #determins if user wants to exit program
    if(sos == -1):
        print("Thank you. Program over!")
        condition = False
    
    #breaks out of code if user inputs number > -1 
    elif(sos < -1):
        print("Invalid input. PLease enter a value > 1")
    
    #calculates the sos of number
    else:
        final_num = 0 
        for i in range(sos):
            square = (i + 1) * (i + 1)
            final_num = square + final_num
        print(final_num)