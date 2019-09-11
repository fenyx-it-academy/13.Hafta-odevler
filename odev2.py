input1=input("Lutfen birinci ve ikinci listedeki elaman sayisini aralarinda bir bosluk olucak sekilde '3 5' sekli ile giriniz:")
input1=input1.rstrip().split()
number1=int(input1[0])
number2=int(input1[1])
value1=[]
value2=[]
for i in range(number1):
    input2=int(input("Lutfen birinci listenin elamanini giriniz:"))
    value1.append(input2)
for i in range(number2):
    input3=int(input("Lutfen ikinci listenin elamanlarini giriniz:"))
    value2.append(input3)
def firstlistcheck():
    global value1
    liste=[]
    value1.sort()
    deger=value1[-1]
    deger1=deger
    while True:
        liste1=[]
        for i in value1:
            if deger%i==0:
                liste1.append(1)
            else:
                liste1.append(0)
        if 0 in liste1:
            deger=deger+deger1
            continue
        else:
            return deger
def secondlistcheck():
    global value2
    deger=firstlistcheck()
    deger1=deger
    sayilar=[]
    while True:
        liste1=[]
        for i in value2:
            if i<deger:
                return sayilar
            else:
                pass
            if i%deger==0:
                liste1.append(1)
            else:
                liste1.append(0)
        if 0 in liste1:
            deger+=deger1
            continue
        else:
            sayilar.append(deger)
            deger+=deger1
            continue
def getTotalX():
    sonuc=secondlistcheck()
    return print("verilen listelere gore iki liste arasi sayilar {} tane olup bu sayilar:".format(len(sonuc)),sonuc)
for i in value1:
    for k in value2:
        if i>k:
            sonuc=0
            print(sonuc)
            quit()
getTotalX()


