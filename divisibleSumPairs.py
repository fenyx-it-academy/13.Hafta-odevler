
def divisibleSumPairs(n, k, ar):

    a=[(ar[i]+ar[-j]) for i in range(n) for j in range(1,len(ar)-i) if (ar[i]+ar[-j])%k==0]
    print(len(a))

nk = input().split()
n = int(nk[0])
k = int(nk[1])
ar = list(map(int, input().rstrip().split()))
result = divisibleSumPairs(n, k, ar)
