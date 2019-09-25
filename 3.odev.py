##3.odev
##n sayılı bir liste ( ar = [ ar[0], ar[1], ..., ar[n-1] ] ) ve pozitif
##bir tamsayı olan k sayısının verildiği bir durumda i<j ve ar[i] + ar[j]’nin
##k sayısına tam bölündüğü sayı çiftlerinin ( i, j ) sayısını bulunuz.
##Fonksiyon Tanımı
##Fonksiyon koşulları sağlayan sayı çiftlerinin sayısını integer olarak
##vermelidir. Fonksiyon 3 parametre almaktadır:
##● n: listenin eleman sayısı
##● ar: array(liste)
##● k: sayı çiftlerinin toplamının böleni


def divisibleSumPairs(n, k, ar):
    liste=[]
    for i in range(n) :
        for j in range(i+1,n) :
            if (ar[i]+ar[j]) % k == 0 and i<j :
                liste+=[(i,j)]
    return len(liste)
            
nk = input('deger1').split()

n = int(nk[0])

k = int(nk[1])

ar = list(map(int, input('deger2').rstrip().split()))

result = divisibleSumPairs(n, k, ar)

print(result)









    
