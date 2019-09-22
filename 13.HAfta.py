
#1.Odev
def staircase(f):
    for i in range(1, f + 1):
        print(('#'*i).rjust(f,' '))
n = int(input("Pleasa enter  a number: "))
staircase(n)


# 2. Odev
def getTotalX():
    first_multiple_input = input('aralarinda bosluk birakarak birinci ve '
                                 'ikinci listenin elaman sayilarini giriniz:').split()  #split ile bosluklardan ayirdik

    n = int(first_multiple_input[0])
    m = int(first_multiple_input[1])
    birinci_liste = list(map(int, input('aralarında bosluk bırak ve 1.lıste elemanlarını gır :').split()))
    ikinci_liste = list(map(int, input('aralarında bosluk bırak ve 2.lıste elemanlarını gır  :').split()))

    b = []
    a = []

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

# 3.Odev

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
AB = input('aralarinda bosluk birakarak A ve B sayilarini giriniz').split()
CD = list(map(int,input('aralarinda bosluk birakarak listenin elemanlarini giriniz:').split()))
divisibleSumPairs()