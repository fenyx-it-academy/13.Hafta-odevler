##odev 3
nk = input(":").split()
n = int(nk[0])
k = int(nk[1])
ar = list(map(int, input(":").rstrip().split()))
##result = divisibleSumPairs(n, k, ar)
def divisibleSumPairs(n, k, ar):
    sayac=0
    for i in range (len(ar)):
        for s in range(i + 1, len(ar)):
            if ((ar[i] + ar[s]) % k == 0):
                sayac += 1
    return sayac
result = divisibleSumPairs(n, k, ar)
print(result)
