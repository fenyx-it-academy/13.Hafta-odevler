n = int(input("Listenizin eleman sayisini giriniz (2 <= n <= 100) : "))
k = int(input("Boleni giriniz (1 <= n <= 100) : "))

ar = list(range (1, n + 1))

bolen_list = []

for x in ar:
    for y in ar:
        if (x + y) % k == 0 and x < y :
            cift = [x, y]
            bolen_list.append(cift)

print(bolen_list)
print(len(bolen_list))