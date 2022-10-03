"""
File:    gasbuddy1.py
Author:  Ouwen Dai
Date:    10/1/22
Section: 56
E-mail:  odai1@umbc.edu
Description: finds the sum of squares of int input by user

"""

from glob import iglob


if __name__ == '__main__':
    
    #stores number of gas stations the user wants to input
    num_gas = int(input("How many gas stations will you store?"))

    #stores gas prices for each gas station
    gas_list = list()

    #user inputs prices for each gas station
    for i in range(num_gas):
        print("What is the gas price at station",i + 1)
        gas_price = float(input(""))
        gas_list.append(gas_price)
    
    low_gas = 0

    gas_station = 1


      #checks the lowest price
    for i in range(len(gas_list)):
        
       if(gas_list[i] > low_gas):
           low_gas = gas_list[i] 
    
        if:
            gas_station += i
            print(gas_station)
    
    print("The lowest price of gas found was station #", gas_station , "at $", low_gas)