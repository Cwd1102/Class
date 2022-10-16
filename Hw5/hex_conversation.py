"""
File:    hex_converstaion.py
Author:  Ouwen Dai
Date:    10/16/22
Section: 56
E-mail:  odai1@umbc.edu
Description: Takes user input and tells if every index is a valid Hexadecimal value

"""

if __name__ == '__main__':
    value = input("Please enter a hexadecimal value:")

    #reference to turn characters into int value
    char_list = ["A" , "B" , "C" , "D" , "E" , "F"]
 
    number_list = []

    #Converts all string to hexadecimal values (Turns A to 10 B to 11 etc.)
    #appends all converted string to new list
    for i in range(len(value)):
        condition = True
        while condition:
            if value[i].isdecimal():
               change = int(value[i])
               number_list.append(change)
               condition = False
            #Turns the characters into numeric values
            else:
                for x in range(len(char_list)):
                    if value[i].capitalize() == char_list[x]:
                        change = 10 + x
                        number_list.append(change)
                condition = False
    
    #calculates the final hexadecimal numbers
    fin_num = 0
    for i in range(len(number_list)):
        hex_val = number_list[-i - 1]
        square = hex_val * (16 ** i)
        fin_num += square
    print(f"The decimal value of that is: {fin_num}")
