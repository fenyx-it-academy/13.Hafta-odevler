def getTotalX(a, b):
    sayac=0
    # burdan ilk listedeki en buyuk ile son listedeki en kucuk degerler arasindaki tum degerleri i ye aktariyoruz.
    for i in range(max(arr),min(brr)+1):
        lista=[i%x for x in arr]  # burda alinan i degerlerini ilk listedeki degerleri bolup kalanladan liste olusturuyoruz.
        liste=[x%i for x in brr]  # burda alinan i degerlreiyle son listedeki degerleri boluyoruz kalanlari liste yapiyoruz.
        if lista.count(0)+liste.count(0)==n+m: #burda bolumlerden kalanlarin hepsinin 'sifir' olup olmadigini cek ediyoruz.
            sayac+=1                    # eyer tum kalanlar sifir ise sayaci artiriyoruz.
    return sayac

first_multiple_input = input("listelerinizin uzunluklari icin iki sayi giriniz:").rstrip().split()
n = int(first_multiple_input[0])
m = int(first_multiple_input[1])
arr = list(map(int, input("ilk listenizin elemanlari").rstrip().split()))
brr = list(map(int, input("son listenizin elemanlari:").rstrip().split()))
total = getTotalX(arr, brr)
print(total)