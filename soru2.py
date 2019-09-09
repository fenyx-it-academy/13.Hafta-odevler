#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
    bOrtakBolenleri = []
    bOrtakBolenlerindenAyiBolenler = []
    aNinEnBuyugu = max(a)
    bNinEnKucugu = min(b)
    for i in range(aNinEnBuyugu, bNinEnKucugu + 1):
        bolenler = list(filter(lambda siradaki: siradaki % i == 0, b))
        if len(bolenler) == len(b):
            bOrtakBolenleri.append(i)
    for bBoleni in bOrtakBolenleri:
        bolenler = list(filter(lambda siradaki: bBoleni % siradaki == 0, a))
        if len(bolenler) == len(a):
            bOrtakBolenlerindenAyiBolenler.append(bBoleni)
    return len(bOrtakBolenlerindenAyiBolenler)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
