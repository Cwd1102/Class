"""
File:    hex_validation.py
Author:  Ouwen Dai
Date:    10/16/22
Section: 56
E-mail:  odai1@umbc.edu
Description: Takes user input and tells if every index is a valid Hexadecimal value

"""

if __name__ == '__main__':
    
    val = input("Please enter a hexadecimal value:")

    check = "ABCDEF123456789"

    index_num = 0
    
    #checks the string len() times
    for i in range(len(val)):
        val.upper()
        if val[i : i + 1] in check:
            print(f"Index [{index_num}] : {val[i : i + 1]} : is a VALID Hexadecimal")
            index_num += 1
        else:
            print(f"Index [{index_num}] : {val[i : i + 1]} : is an INVALID Hexadecimal")
            index_num += 1