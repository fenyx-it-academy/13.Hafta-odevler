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
    # Write your code here
    nlist = [i for i in range(max(a), min(b) + 1)]
    clist = []
    clistlast = []
    for i in nlist:
        for j in range(0, len(a)):
            if i % a[j] != 0:
                break
            elif i % a[j] == 0:
                if j == (len(a) - 1):
                    clist.append(i)

    for i in clist:
        for j in range(len(b)):
            if b[j] % i != 0:
                break
            elif b[j] % i == 0:
                if j == (len(b) - 1):
                    clistlast.append(i)
    return len(clistlast)


first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

arr = list(map(int, input().rstrip().split()))

brr = list(map(int, input().rstrip().split()))

total = getTotalX(arr, brr)
print(total)