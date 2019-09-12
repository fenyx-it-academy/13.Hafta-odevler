import math
import os
import random
import re
import sys

# Complete the divisibleSumPairs function below.
def divisibleSumPairs(n, k, ar):
    divisor = []
    for i in range(n):
        for j in range(n):
            if i < j and (ar[i] + ar[j])%k == 0:
                divisor.append((ar[i],ar[j]))
    return print(len(divisor))

if __name__ == '__main__':
    fptr = open("divisible.txt", 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    ar = list(map(int, input().rstrip().split()))

    divisor = divisibleSumPairs(n, k, ar)

    fptr.write(str(divisor) + "\n")

    fptr.close()