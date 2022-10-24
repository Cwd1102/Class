"""
File: wind2.py
Author: Ouwen Dai
Date: 9/19/22
Lab Section: 56
Email:  odai1@umbc.edu
Description:  This program tells the user the catagory of storm based on their input(Floats)

"""

def main():

    wind = -1

    wind = float(input("What is the wind speed?"))

    if(wind < 96):
        print("The wind's speed category is Minimum")

    elif(wind < 111):
        print("The wind's speed category is Moderate")

    elif(wind < 131):
        print("The wind's speed category is Extensive")
    
    elif(wind < 155):
        print("The wind's speed category is Extreme")
    
    else:
        print("The wind's speed category is Catastrophic")

main()
