"""
File:    prime.py
Author:  Ouwen Dai
Date:    10/4/22
Section: 56
E-mail:  odai1@umbc.edu
Description: finds the gas station with the cheapest price

"""

if __name__ == '__main__':
    
    prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61]

    value = int(input("What value are we looking for primes?"))

    org_value = value

    prime_final = list()

    condition = True

    i = 0

    if(value > 0):
        while(condition):
            if(value == 1):
                condition = False
            elif((value % prime[i]) == 0):
                value = value / prime[i]
                prime_final.append(prime[i])
                i = 0
            i += 1
    else:
        print("Please enter a valid value > 0")
    
    print("The prime factors for", org_value , "are :", prime_final)

