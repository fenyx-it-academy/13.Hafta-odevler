print(14 * " >", "\t n.B.a. \t", "< " * 14, "\n\n\n")


match_pairs = []                               # bunun yerine dongunun icinde sayac kullanarakta ayni sonucu elde ederiz

def divisibleSumPairs(n, k, ar):
    for i in range(0, n):                       # 0 dan baslayip input edilen n ye kadar sayilar taransin
        for j in range(i+1, n):                 # burda i < j constraint ini, j yi (i+1,n) icinde aratarak sartlar elde edilmis oluyor
            if (ar[i] + ar[j]) % k == 0:        # sartlari saglayan ciftler in toplamlari k ya bolumunden kalan sifiri veriyorsa
                match_pairs.append((i, j))      # bu sartlardaki ikilileri yukarda tanimladigimiz listeye ekle
    print(match_pairs)                          # opsiyonel eklendi gormek icin
    return print(len(match_pairs))              # kac adet oldugunu yazdir


nk = input("Enter size of array a: ").split()
ar = list(map(int, input("Enter n(elements of size of array a): ").split()))

n = int(nk[0])
k = int(nk[1])

divisibleSumPairs(n, k, ar)
