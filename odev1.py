def staircase(n):
    x= 1
    while n > 0:
        print((n-1)*' ' + x*'#')
        n -= 1
        x += 1
while True:
    try:
        n = int(input("Kac basamakli merdiven istediginizi rakamla giriniz: "))
        if n<1 or n>100:
            print("1-100 arasi bir rakam giriniz\n")
            continue
        else:
            staircase(n)
            break
    except:
        print("Yanlis giris tekrar deneyiniz..\n")
