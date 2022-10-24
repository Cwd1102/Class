"""
File:    circular.py
Author:  Ouwen Dai
Date:    10/18/22
Section: 56
E-mail:  odai1@umbc.edu
Description: Determines rotational offset of a string

"""



if __name__ == '__main__':
    string = input("Enter a string:")
    string = string.split()
    string = "".join(string)
    string = string.lower()
    new_string = []
    check = 0
    
    for i in range(len(string )):
        new_string = []
        for x in range(len(string)):
            new_string.append(string[(-1 * i) + x])
            temp_string = "".join(new_string)
            if temp_string == string and i != 0:
                print(f"{string} is a rotation with offset {i}")
                check = 1
    if check == 0:
        print("There are no rotations of the string.")