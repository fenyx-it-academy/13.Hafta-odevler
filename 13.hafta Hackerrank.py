####Odev 1 - Staircase

def staircase(n):
    for i in range(1, n + 1):
        print(' ' * (n - i) + '#' * i)

a=staircase(10)
print(a)





####Odev 2 - Between two sets

def getTotalX(a, b):
    b_bolenler= []
    a_bolenler = []

    for i in range(max(a), min(b) + 1):
        bolenler = list(filter(lambda x: x % i == 0, b))
        if len(bolenler) == len(b):
            b_bolenler.append(i)
    for k in b_bolenler:
        bolenler = list(filter(lambda x: k % x == 0, a))
        if len(bolenler) == len(a):
            a_bolenler .append(k)
    return len(a_bolenler)





####Odev 3 - Divisible Sum Pairs

def divisibleSumPairs(n, k, ar):
    result = 0
    for i in range(n):
        for j in range(n):
            if i < j:
                if (int(ar[i])+int(ar[j])) % k == 0:
                    result += 1
            else:
                continue
    return print(result)











