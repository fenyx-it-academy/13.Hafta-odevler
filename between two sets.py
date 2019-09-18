def getTotalX(a,b):
    bolen = []
    ortak = []
    for i in b:
        for x in range(max(a),min(b)+1):
            if i % x == 0:
                bolen.append(x)
    for z in bolen:
        if bolen.count(z) == len(b) and z not in ortak:
            ortak.append(z)
    print(len(ortak))
a = [2, 6]
b = [24, 36]
getTotalX(a,b)


