def merdiven(y):
    x= 1
    while y > 0:
        print((y-1)*' ' + x*'#')
        y -= 1
        x += 1
while True:
    try:
        y = int(input("basamak sayısını giriniz: "))
        if y<1 or y>100:
            print("1-100 arasi bir rakam giriniz\n")
            continue
        else:
            merdiven(y)
            break
    except:
        print("hatalı giriş yaptınız tekrar deneyiniz.5..\n")
