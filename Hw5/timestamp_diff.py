"""
File:    timestamp_diff.py
Author:  Ouwen Dai
Date:    10/16/22
Section: 56
E-mail:  odai1@umbc.edu
Description: Takes user input and tells if every index is a valid Hexadecimal value

"""
if __name__ == '__main__':
    
    #takes input for the two timestamps
    time_1 = input("Please enter timestamp #1:")
    time_2 = input("Please enter timestamp #2:")

    #stores final hour, minute, seconds difference 
    seconds = 0
    minute = 0
    hour = 0

    #calculates the second difference
    if int(time_2[6 :] < time_1[6 :]):
        seconds = (int(time_2[6 :]) - int(time_1[6 :])) + 60
        print(seconds)
        minute = -1
    else:
        seconds = int(time_2[6 :]) - int(time_1[6 :])
    

    #calculates the minute difference
    if int(time_2[3 : 5] < time_1[3 : 5]):
        minute = (int(time_2[3 :5]) - int(time_1[3 : 5])) + (60 + minute)
        hour = -1
    else:
        minute = int(time_2[3 : 5]) - int(time_1[3 : 5]) + minute 
    

    #calculates the hour difference
    if int(time_2[0 : 2] < time_1[0 : 2]):
        hour = (int(time_2[0 :2]) - int(time_1[0 : 2])) + (24 + hour)
    else:
         hour = (int(time_2[0 :2]) - int(time_1[0 : 2])) + hour
    

    #turnsall numbers into seconds
    final_sec = (hour * 3600) + (minute * 60) + seconds

#prints the final results
print(f"That is {hour} hour(s), {minute} minute(s), and {seconds} seconds")
print(f"But in seconds that is: {final_sec}")