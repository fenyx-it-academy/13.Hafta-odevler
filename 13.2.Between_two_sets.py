print(14 * " >", "\t n.B.a. \t", "< " * 14, "\n\n\n")


def getTotalX(a, b):

    firstarray_b_divided = []                                    # b dizisine bolunebilenleri buraya ekle
    secondarray_b_divided_a = []                                 # b dizisine bolunup sonra a ya bolunenleri buraya ekle

    for v in range(max(a), min(b) + 1):                          # a dizisinin enbuyuk degeri ile b dizisinin enkucuk degerinin arasindaki degerleri kontrol etmememiz lazim
        divides = list(filter(lambda x: x % v == 0, b))          # iki dizi arasindaki sayilar ile b dizisindeki sayilarin bolumunden kalan sifir ise
        if len(divides) == len(b):                               # ve b dizisindeki degere esit ise bolunenler listesine ekle
            firstarray_b_divided.append(v)
    for w in firstarray_b_divided:                               # b dizisinde bolunenler bu sefer a dizisindeki elemanlarin bolumunden kalani sifir oluyorsa
        divides = list(filter(lambda x: w % x == 0, a))
        if len(divides) == len(a):                               # ve bu degerler a dizisindeki sayilara esit ise
            secondarray_b_divided_a.append(w)                    # a ve be dizisindeki elemanlara ortak bolunenler kumesine eklensin
    return print(len(secondarray_b_divided_a))


first_multiple_input = input("Enter the size of arrays a and b: ").split()          # burda dizilerin boyutlarini input

n = int(first_multiple_input[0])
m = int(first_multiple_input[1])
arr = list(map(int, input("Enter elements of a: ").split()))                        # a dizisini input
brr = list(map(int, input("Enter elements of b: ").split()))                        # b dizisini input
getTotalX(arr, brr)

# if (n in range(1, 11)) and (m in range(1, 11)):
#     arr = list(map(int, input("Enter elements of a: ").split()))
#     brr = list(map(int, input("Enter elements of b: ").split()))
#     for i in arr or j in brr:
#         if i in range(1, 101) or j in range(1, 101):
#             getTotalX(arr, brr)
