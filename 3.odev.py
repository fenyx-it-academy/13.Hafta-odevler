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

ar = [1,3,2,6,1,2]
k = 3
n=len(ar)
liste = []
for i in ar:
    for j in ar:
        if (i+j) % k == 0 and i<j :
            liste += [(i,j)]
print('sayı çiftleri : ',liste)
print('sayı çiftlerinin ( i, j ) sayısı : ',n)













    
