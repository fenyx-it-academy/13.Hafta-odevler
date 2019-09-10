#ODEV2


first_multiple_input =input().rstrip().split()
arr = list(map(int, input().rstrip().split()))
brr = list(map(int, input().rstrip().split()))

# l=[]
# #bizden istenen ilk kumenin elemanlarinin katlari,ikincinin tam bolenleri
# for i in range(max(arr),min(brr)+1):
# #bu sayilar ilk kumenin elemanlarinin en buyugune esit veya daha buyuk
# #ikinci kumenin en kucuk elemanina esit veya daha kucuk
# once ilk kumenin elamnlarinin bu araliktaki katlarini bulalim
#     for j in arr:
#         if i%j==0:
#             l.append(i)
#bu islemin tek satir hali asagidadir(liste).bu listede birinci listenin elemanlarinin katlari tekrarli yaziliyor
# eger bir sayi birnci listenin eleman sayisi kere tekrar etmisse ortak kattir

liste=[i for i in range(max(arr),min(brr)+1) for j in arr if i%j==0]
b=[i for i in liste if liste.count(i)==int(first_multiple_input[0])]

#ayni dusunce sistemi ikinci kumenin ortak bolenleri icinde kullanilirsa:
# list2=[]
# for i in set(b):
#     for j in brr:
#         if j%i==0:
#             list2.append(i)
#             print(list2)
# tek satira indirgenmis hali liste2 dir
liste2=[i for i in set(b) for j in brr if j%i==0]
c=[i for i in liste2 if liste2.count(i)==int(first_multiple_input[1])]
# print(c)
print(len(set(c)))

#ODEV3

nk = list(map(int, input().rstrip().split()))  # iki sayi girilecek.1)eleman sayisi  2)hangi sayinin kati olacak
ar = list(map(int, input().rstrip().split()))
# liste=[]
# for i in range(nk[0]):
#     for j in range(nk[0]):
#         if (ar[i]+ar[j])%nk[1]==0 and i<j:

# #listedeki iki sayinin toplami aliniyor ve (i!=j den) kendisiyle eslesmiyor
# #[6,7]gibi bir iki yazildiginda ayni konumdaki 6 ve 7 icin [7,6]yazilmiyor i<j den dolayi

# print([ar[i],ar[j]])
# asagida bu ikililer printlenmiyor.ikililerin listesi olusturulup eleman sayisi printleniyor

liste = [[ar[i], ar[j]] for i in range(nk[0]) for j in range(nk[0]) if (ar[i] + ar[j]) % nk[1] == 0 and i < j]

print(len(liste))
