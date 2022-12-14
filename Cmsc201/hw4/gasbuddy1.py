"""
File:    gasbuddy1.py
Author:  Ouwen Dai
Date:    10/1/22
Section: 56
E-mail:  odai1@umbc.edu
Description: finds the gas station with the cheapest price

"""

if __name__ == '__main__':

    #stores gas prices for each gas station
    gas_list = list()

    #stores unsorted gas_list
    station_list = list()

    #stores value for lowest gas price
    low_gas = 0

    #stores the station number that has the lowest gas
    gas_station = 1

    #true condition for station check while loop
    condition = True

    #true condition for price check while loop
    name = True

    station_num = True

    station = 0

    var = 0

    num_gas = 0

    while(station_num):
        #stores number of gas stations the user wants to input
        num_gas = int(input("How many gas stations will you store?"))
        if (num_gas <= 0):
            print("Invalid number of gas stations")
        else:
            station_num = False

    while(name):
        print("What is the gas price at station", station + 1)
        gas_price = float(input(""))
        if(gas_price < 0):
            print("I wish, but please enter a valid price of gas.")
        else:
            gas_list.append(gas_price)
            station_list.append(gas_price)
            station += 1
            
        if(station == num_gas):
                name = False

    for x in range(len(gas_list)):
        for i in range(len(gas_list) - 1):
            if(gas_list[i] > gas_list[i + 1]):
                num_1 = gas_list[i]
                num_2 = gas_list[i + 1]
                gas_list[i] = num_2
                gas_list[i + 1] = num_1
                low_gas = gas_list[0]

    while(condition):
        if(gas_list[0] == station_list[var]):
            gas_station = var + 1
            condition = False
        var += 1
    
    print("The lowest price of gas found was station #%d at $%.2f" %(gas_station , low_gas))