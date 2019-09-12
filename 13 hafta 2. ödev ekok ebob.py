
import math
import os
import random
import re
import sys
def getTotalX(arr, brr):
    ortakkatlar=[]
    for i in range(max(arr),(min(brr))+1):
        toplam=0
        for k in range(n):
            toplam+= i%arr[k]
        if toplam==0:
            ortakkatlar+=[i]
    ortakbolenler=[]
    for i in range(max(arr),min(brr)+1):
        toplam=0
        for k in range(m):
            toplam+= brr[k]%i
        if toplam==0:
            ortakbolenler+=[i]
    return len(set(ortakbolenler).intersection(set(ortakkatlar)))
            
if __name__ == '__main__':
    ptr = open(os.environ['OUTPUT_PATH'], 'w')
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    m = int(first_multiple_input[1])
    arr = list(map(int, input().rstrip().split()))
    brr = list(map(int, input().rstrip().split()))
    total = getTotalX(arr, brr)
    print(total)
    fptr.write(str(total))
    fptr.close()
