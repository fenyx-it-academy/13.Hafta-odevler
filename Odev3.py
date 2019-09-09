def divisibleSumPairs(n, k, ar):
    result = 0
    k = int(k)
    n = int(n)
    for i in range(0, n):
        for j in range(0, n):
            if i < j:
                if (int(ar[i])+int(ar[j])) % k == 0:
                    result += 1
                else:
                    continue
            else:
                continue
    return print(result)
nk = input().split()
n = int(nk[0])
k = int(nk[1])
# ar = input('ar:').split(' ')
ar = list(map(int, input().rstrip().split()))
divisibleSumPairs(n, k, ar)


