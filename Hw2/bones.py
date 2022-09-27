"""
File: bones.py
Author: Ouwen Dai
Date: 9/19/22
Lab Section: 56
Email:  odai1@umbc.edu
Description:  Calulates the user's paycheck for the week

"""

def main():

    #stores the variable for the # of hours the user has worked
    hours = -1

    #stores the value for the calculated paycheck of the user based on hours
    paycheck = -1

    #asks the user for their hours
    hours = int(input("Hours worked this week:"))
    
    #checks if the user gets overtime, then calulates their paycheck
    if(hours <= 40):
        paycheck = hours * 12.50
        print("Your paycheck for this week will be: $%.2f" %(paycheck))
    
    elif(hours > 40):
        paycheck = ((hours - 40) * 18.75) + (500)
        print("Your paycheck for this week will be: $%.2f" %(paycheck))

main()