def divisibleSumPairs(n, k, ar):
    sayac=0
    for i in range(n):
        for x in range(i+1,n):
            if (ar[i]+ar[x])%k==0:
                sayac+=1
    print(sayac)
nk = input().split()
n = int(nk[0])
k = int(nk[1])
ar = list(map(int, input().rstrip().split()))
result = divisibleSumPairs(n, k, ar)
