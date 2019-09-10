def divisibleSumPairs(n, k, ar):
    sayac=0
    # bolunebilme sayılarını veren degisken
    while len(ar)!=0:
        # liste uzunlugu 0 dan farklı oldugu surece dongu
        b=ar.pop()
        # ar listesinin son elemanı listeden cıkarılıp b'ye atanır
        for i in ar:
            # listenın herbir elemanı icin dongu
            if (i+b)%k==0:
                # listeden alınan herbir eleman listenini geri kalan
                # elmanlarının heb biri ile toplamı k'ya tam bolunuyorsa
                sayac+=1
                # sayacı 1 artır
    print(sayac)
nk = input().split()
# girlen verileri bosluk karakterinden ayır
n = int(nk[0])
# 0 indisli nk yı n'e ata
k = int(nk[1])
# 1 indisli nk yı k'e ata
ar = list(map(int, input().rstrip().split()))
# girilen verileri ayır, int'a cevir ve liste yap
result = divisibleSumPairs(n, k, ar)