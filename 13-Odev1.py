# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 19:50:15 2019

@author: HP
"""

# Staircase

# Program ; Consider a staircase of size :

   #
  ##
 ###
####
 
#Observe that its base and height are both equal to , and the image is drawn using # symbols and spaces. 
#The last line is not preceded by any spaces.

def staircase(n):
    if 0<n<100:
        i=1
        while i<n+1:
            print(' '*(n-i)+'#'*i)
            i+=1
    else:
        print("Please, you must input a integer between 0 and 100 !")

if __name__ == '__main__':
    n=int(input("Enter the number of steps to create the ladder = "))
    staircase(n)
# %%
# Second solution

n=int(input("Enter the number of steps to create the ladderz = "))
i=0
while i<n+1:
    yaz="#"*i
    print(yaz.center(n," "))
    i+=1
