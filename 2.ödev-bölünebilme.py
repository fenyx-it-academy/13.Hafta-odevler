def bölünebilme(n, k, ar):
    list=[]
    for i in range(n):
        for j in range(n):
            if i<j and (ar[i]+ar[j])%k==0:
                list.append(1)
        else:
           pass
    sonuç= len(list)
    print(sonuç)

bölünebilme(4,8,(1, 4, 16, 6 ,8, 12)) 
