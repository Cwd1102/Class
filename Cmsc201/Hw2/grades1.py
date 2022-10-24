"""
File: grades1.py
Author: Ouwen Dai
Date: 9/19/22
Lab Section: 56
Email:  odai1@umbc.edu
Description:  Tells the user their grade based on their input

"""
def main():

    #the value of the user's grade
    grade = -1

    #asksed the user their grade(input replaces placeholder value)
    grade = float(input("Please enter your grade:"))

    #Checks user's grade, then outputs corresponding grade letter
    if(grade >= 96):
        print("The grade would be: A+")

    elif(grade >= 93):
        print("The grade would be: A")

    elif(grade >= 90):
        print("The grade would be: A-")

    elif(grade >= 86):
        print("The grade would be: B+")

    elif(grade >= 83):
        print("The grade would be: B")

    elif(grade >= 80):
        print("The grade would be: B-")

    elif(grade >= 76):
        print("The grade would be: C+")

    elif(grade >= 73):
        print("The grade would be: C")

    elif(grade >= 70):
        print("The grade would be: C-")

    elif(grade >= 66):
        print("The grade would be: D+")

    elif(grade >= 63):
        print("The grade would be: D")

    elif(grade >= 60):
        print("The grade would be: D-")

    else:
        print("The grade would be: F")

main()
    
    
    