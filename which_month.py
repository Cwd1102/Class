"""
File: which_month.py
Author: Ouwen Dai
Date: 9/19/22
Lab Section: 56
Email:  odai1@umbc.edu
Description:  Calculates the user's current month by their desiered months ahead then outputs
the respective month

"""

def main():

    #stores the user's current month
    current_month = -1

    #stores the value for how many months the user wants to go forward
    forward_month = -1

    #the final calculated month stored as an integer
    final_month_out = -1

    #asks the user their current month the assignes it to the var.
    current_month = int(input("What is the current month?:"))
    
    
    
    #checks if the inputted month is valid, if valid, code goes onto else statement
    if(current_month > 12):
        print("That is not a month between 1 and 12")
    
    else:
        #asks the user how many months they want to go forward
        forward_month = int(input("How many months in the future should we go?"))



    #calcuates the final month by adding current_month and foward_month
    # two values then divided by the floor operator 12(how many times forawrd_month goes over a year )\
    #then multiplies it by 12 to change from years back to months
    #Then finally subtracted current_month + foward_month by final_month_1 to get final_month_out
    if((current_month <= 12) & (current_month + forward_month > 12)):
        final_month_1 = ((current_month + forward_month) // (12)) * (12)
        final_month_out =  (current_month + forward_month) - final_month_1

    #runs if the future year does not go over 12
    elif((current_month <= 12) & (current_month + forward_month <= 12)):
        final_month_out = (current_month + forward_month)
        
    

    
    #takes the calculated value and checks which month the number corresponds to
    if(final_month_out == 1):
        print("The current month will be January")
    
    elif(final_month_out == 2):
        print("The current month will be February")

    elif(final_month_out == 3):
        print("The current month will be March")

    elif(final_month_out == 4):
        print("The current month will be April")

    elif(final_month_out == 5):
        print("The current month will be May")

    elif(final_month_out == 6):
        print("The current month will be June")

    elif(final_month_out == 7):
        print("The current month will be July")

    elif(final_month_out == 8):
        print("The current month will be August")

    elif(final_month_out == 9):
        print("The current month will be September")

    elif(final_month_out == 10):
        print("The current month will be October")

    elif(final_month_out == 11):
        print("The current month will be November")

    elif(final_month_out == 12):
        print("The current month will be December")
           
main()