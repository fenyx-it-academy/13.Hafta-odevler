def divisibleSumPairs(n, k, ar):
    pairs_ar=0
    for i in range(0,len(ar)):
        for x in range(0,len(ar)):
            sum_ar=ar[i]+ar[x]
            if i<x and sum_ar%k==0:
                pairs_ar+=1
    return pairs_ar
#nk = input().split()
#n = int(nk[0])
#k = int(nk[1])
#ar = list(map(int, input().rstrip().split()))
n=6
k=3
ar=[1,3,2,6,1,2]
result = divisibleSumPairs(n, k, ar)
print(result)