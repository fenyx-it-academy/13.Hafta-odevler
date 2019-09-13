print('b.')
'''
n sayılı bir liste ( ar = [ ar[0], ar[1], ..., ar[n-1] ] ) ve pozitif bir tamsayı olan k sayısının verildiği
bir durumda i<j ve ar[i] + ar[j]’nin k sayısına tam bölündüğü sayı çiftlerinin ( i, j ) sayısını
bulunuz.
Örnek: ar = [1, 2, 3, 4, 5, 6] ve k = 5. Yukarıda belirtilen koşulu sağlayan sayı çiftleri
[1, 4], [2, 3] ve [4, 6].
Fonksiyon Tanımı
Fonksiyon koşulları sağlayan sayı çiftlerinin sayısını integer olarak vermelidir.
Fonksiyon 3 parametre almaktadır:
● n: listenin eleman sayısı
● ar: array(liste)
● k: sayı çiftlerinin toplamının böleni
Input Formatı
İlk input satırı boşluk ile ayrılmış 2 integerdan oluşmalıdır: n ve k.
İkinci input satırı birbirinden boşlukla ayrılmış ve listenin elemanlarını tanımlayan n tane liste
elemanından oluşmalıdır.
Output Formatı
Yukarıda belirtilen koşulları sağlayan sayı çiftlerinin sayısını verin.
Örnek Input
6 3
1 3 2 6 1 2
Örnek Output
5
'''

def divisibleSumPairs():
    n = int(nk[0])
    k = int(nk[1])
    b = 0
    for j in range(len(ar)):
        for i in range(len(ar)):
            if i < j and (ar[i] + ar[j]) % k == 0:
                b += 1
    print(b)
print('''
Örnek Input
6 3
1 3 2 6 1 2
Örnek Output
5''')
nk = input('aralarinda bosluk birakarak n ve k sayilarini giriniz').split()
ar = list(map(int,input('aralarinda bosluk birakarak listenin elemanlarini giriniz:').split()))
divisibleSumPairs()
