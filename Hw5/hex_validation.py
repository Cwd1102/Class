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
    print(val)

    index_num = 0
    
    for i in val:
        if i.isalnum():
            print(f"Index [{index_num}] : {i} : is a VALID Hexadecimal")
            index_num += 1
        else:
            print(f"Index [{index_num}] : {i} : is an INVALID Hexadecimal")
            index_num += 1
