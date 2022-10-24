"""
File:    wind.py
Author:  Ouwen Dai
Date:    9/19/22
Section: 56
E-mail:  Odai1@umbc.edu
Description: Tells the user category of storm based on wind speed
"""

def main():

  wind = -1

  wind = int(input("What is the wind speed?"))

  if(wind< 74):
    print("wind is good")

  elif(wind <= 95):
    print("The wind's speed category is Minimum")
  
  elif(wind<= 110):
    print("The wind's speed category is Moderate")

  elif(wind<= 130):
    print("The wind's speed category is Extensive")

  elif(wind<= 155):
    print("The wind's speed category is Extreme")

  else:
    print("The wind's speed category is Catastrophic")

main()
