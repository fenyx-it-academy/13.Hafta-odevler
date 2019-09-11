def divisibleSumPairs(n, k, ar):
    counter = 0
    for i in range(n):
        for b in range(i+1,n):
            if (ar[i]+ar[b])%k==0:
                counter+=1
    print(counter)


nk = input().split()
n = int(nk[0])
k = int(nk[1])
ar = list(map(int, input().rstrip().split()))

result = divisibleSumPairs(n, k, ar)