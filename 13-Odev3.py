# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 19:51:08 2019

@author: HP
"""
# Divisible Sum Pairs
# Program;You are given an array of n integers,ar[...] , and a positive integer, k. 
# Find and print the number of (i,j) pairs where i<j and ar[i] +ar[j]  is divisible by .


# Complete the divisibleSumPairs function 
def divisibleSumPairs(n, k, ar):
    count=0
    for i in range(len(ar)):
        for j in range(1,len(ar)):
            if (i<j) and (ar[i]+ar[j])%k==0:
                print(i,j)
                count+=1
    print(count)
    
if __name__ == '__main__':
    nk = input("Liste boyutu ve bolunecek elemani bir bosluk ile giriniz ;").split()
    n = int(nk[0]) ; k = int(nk[1])
    ar = list(map(int, input("Liste elemanlarini giriniz =").rstrip().split()))
    divisibleSumPairs(n, k, ar)
