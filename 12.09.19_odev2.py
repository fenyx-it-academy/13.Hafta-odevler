a = [2, 6]
b = [24, 36]

bolenler = []
ortak_bolenler = []

small_no = max(a)
big_no = min(b)

division = range(small_no, big_no + 1)

for i in b:
    for x in division:
        if i % x == 0:
            bolenler.append(x)

for z in bolenler:
    if bolenler.count(z) == len(b) and z not in ortak_bolenler:
        ortak_bolenler.append(z)

print(ortak_bolenler)
print(len(ortak_bolenler))

