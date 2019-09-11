# nk= 6 3
# n = 6
# k = 3
# ar=[1,2,3,4,5,6]
def divisibleSumPairs(n, k, ar):
    liste=[(i,j) for i in range(n-1) for j in range(i+1,n) if (ar[i]+ar[j])%k==0]
    return len(liste)
nk = input().split()
n = int(nk[0])
k = int(nk[1])
ar = list(map(int, input().rstrip().split()))
result = divisibleSumPairs(n, k, ar)
print(result)
# nk: liste eleman sayisi ve toplamlari bolecek sayiyi tutan degisken
# n: liste kac eleman olacak
# k: toplamlari bolecegimiz sayi
# ar: islem uygulayacagimiz liste
