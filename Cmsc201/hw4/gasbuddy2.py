"""
File:    gasbuddy2.py
Author:  Ouwen Dai
Date:    10/3/22
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

    #stores the station number
    station = 0

    #variable for while loops below
    var = 0

    #final number for average price
    avg = 1

    #all gas prices added up
    sum = 0

    #user inputs prices for each gas station, types quit to end loop
    #reclasses type to float if quit not dected
    #input starts off as string
    while(name):
        print("What is the gas price at station", station + 1 ,"(quit to exit)")
        gas_price = input("")

        if(gas_price == "quit"):
            name = False
        else:
            gas_price = float(gas_price)
        if(type(gas_price) == float):    
            if(gas_price < 0):
                print("I wish, but please enter a valid price of gas.")
            else:
                gas_list.append(gas_price)
                station_list.append(gas_price)
                station += 1

    #sorts list by looping the loop to ensure accuracy 
    for x in range(len(gas_list)):
        for i in range(len(gas_list) - 1):
            if(gas_list[i] > gas_list[i + 1]):
                num_1 = gas_list[i]
                num_2 = gas_list[i + 1]
                gas_list[i] = num_2
                gas_list[i + 1] = num_1
                low_gas = gas_list[0]
    
    #calculates the average of the gas prices
    for i in range(len(gas_list)):
        sum = sum + gas_list[i]
    
    avg = sum / (len(gas_list))

    #finds respective gas station number for highest price 
    while(condition):
        if(gas_list[0] == station_list[var]):
            gas_station = var + 1
            condition = False
        var += 1

    var = 0

    condition = True

    #finds respective gas station number for highest price 
    while(condition):
        if(gas_list[len(gas_list) - 1] == station_list[var]):
                highest_gas_station = var + 1
                condition = False
        var += 1
    
    print("The lowest price of gas found was station #%d at $%.2f" %(gas_station , low_gas) )
    print("The highest price of gas found was station #%d at $%.2f" %(highest_gas_station , gas_list[len(gas_list) - 1]))
    print("The average gas price was $%.2f" %(avg))