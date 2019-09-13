############1##################3

#!/bin/python3
def staircase(n):
    for i in range(n):
        print(((i+1)*'#').rjust(n))    
        
a = int(input())
if 0< a< 100 or  a ==100:
    staircase(a)
else:
    print('Entered value is not in range.')


###########2#########
#BU EKSIK, YAPAMADIM BUGUN YAPIP ATACAGIM
betw_arrs = []

def getTotalX(a, b):
    n_and_m = input("""Please indicate a number from 1 and including 10 for
the numbers each group gonna take: """).rstrip().split()        #n ve meyi ayir
    a = list(map(int, input('Enter th elements of a:').rstrip().split()))  #a'yi eleman eleman bol ve hepsinin integer yap
    b = list(map(int, input('Enter th elements of b: ').rstrip().split()))  #byi de
    if  a[i] > 100 or b[i] > 100:
        print('type smth between 1 and 100')
    else:
        for i in range(min(a), max(b)):
            if betw_arrs[i] % a[i] == 0 and b[i] % betw_arrs[i] == 0:
                betw_arrs.append(i)

            return len(betw_arrs)

getTotalX(a, b)
#############3################
#BU EKSIK, YAPAMADIM BUGUN YAPIP ATACAGIM

ar = []
len(ar) = n


def divisibleSumPairs(n, ar, k):
    f_l = list(map(int(), input('the lenght of the array, and the integer ')).rstrip.split())
    s_l= list(map(int(), input('the values of arr').rstrip().split()))

    for i in :
        if ar[i] > ar[j] and (ar[i] + ar[j]) % k == 0:
    i =
    j =
    print((f'({i}, {j})')

divisibleSumPairs()

