print('b.')
'''
Verilen iki listeden ilk listenin tüm elemanlarının tam bölebildiği bir sayıların, ikinci listenin tüm
elemanlarını tam bölebildiği durumların sayısını tespit eden bir fonksiyon yazınız.
Bu tür sayılara iki liste arası sayılar diyeceğiz. Bu tür sayıların sayısını tespit etmeniz
gerekmektedir.
Örnek:
İki liste verildiğini düşünelim:
a = [2, 6]
b = [24, 36]
Bu durumda iki liste arası sayılar 6 ve 12’dir.
İlk değer (6) için:
6 % 2 = 0
6 % 6 = 0
24 % 6 = 0
36 % 6 = 0
İkinci değer (12) için:
12 % 2 = 0
12 % 6 = 0
24 % 12 = 0
36 % 12 = 0
Fonksiyon Tanımı
getTotalX fonksiyonunu tamamlayarak iki liste arası sayıların miktarını verecek şekle getiriniz.
getTotalX fonksiyonu iki parametre almaktadır:
a: integerlardan oluşan bir liste
b: integerlardan oluşan bir liste
Input Formatı
İlk input satırı boşluklarla birbirinden ayrılmış iki integerdan (m ve n) oluşmalıdır. Bu integerlar a
ve b listelerinin eleman sayılarını belirleyecektir.
İkinci input satırı birbirinden boşlukla ayrılmış, birbirinden farklı ve a listesinin elemanlarını ( a
[ i ] ) oluşturan n tane integerdan oluşmalıdır. Koşul: 0 <= i <=n.
Üçüncü input satırı birbirinden boşlukla ayrılmış, birbirinden farklı ve b listesinin elemanlarını
( b[ j ] ) oluşturan m tane integerdan oluşmalıdır. Koşul: 0 <= j <=m.
Kısıtlamalar:
1 <= n,m <=10
1 <a [i] <100
1 <= b[j] <=100
Output Formatı:
a ve b listelerinin arasında olan (yukarıda belirtilen koşulları sağlayan) sayıların miktarını output
olarak vermeniz gerekmektedir.
Örnek Input:
2 3
2 4
16 32 96
Örnek Output:
3
Açıklama:
2 ve 4 (a listesinin elemanları) sayıları 4, 8, 12 ve 16 sayılarına tam bölünmektedir.
4, 8 ve 16 sayıları 16, 32, 96 sayılarına (b listesinin elemanları) tam olarak bölünmektedir.
4, 8 ve 16 sayıları a listesinin elemanları tarafından tam bölünebilen ve b listesinin elemanlarını
tam bölebilen sayılar olduğundan cevap 3 olacaktır.
'''
def getTotalX():
    first_multiple_input = input('aralarinda bosluk birakarak birinci ve '
                                 'ikinci listenin elaman sayilarini giriniz:').split()  #split ile bosluklardan ayirdik
    n = int(first_multiple_input[0])
    m = int(first_multiple_input[1])
    birinci_liste = list(map(int, input('birinci listenin elamanlarini aralarinda boslik birakarak giriniz :').split()))
    ikinci_liste = list(map(int, input('ikinci listenin elamanlarini aralarinda boslik birakarak giriniz :').split()))
    b = []
    a = []
    # ilk listenin max elamani ile ikinci listenin min elamani arasindaki sayilari sayilari bulduk
    # range ile buldugumuz elamanlari birinci listenin elamanlarinin ikisinede bolunenleri ayikladik
    for i in range(max(birinci_liste), min(ikinci_liste) + 1):
        for j in birinci_liste:
            if i % j != 0:
                break
        else:
            a.append(i)
    #ikinci listenin elamanlarinin hepsini bolenlerini bulduk
    for j in a:
        for i in ikinci_liste:
            if i % j != 0:
                break
        else:
            b.append(j)
    # birinci listeye bolunen ikinci lisyeyi bolen elamanlarin sayisi
    print(f'birinci listeye bolunen,ikinci lisyeyi bolen elamanlarin sayisi:{len(b)}')
getTotalX()
