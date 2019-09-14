def divisibleSumPairs(n, k, ar):
    list=[]
    for i in range(n):
        for j in range(n):
            if i<j and (ar[i]+ar[j])%k==0:
                list.append(1)
        else:
           pass
    result= len(list)
    print(result)
    # lis1=random.sample(list(i for i in range(n)),n)
    # print(lis1)

divisibleSumPairs(6,3,(1, 3, 2, 6 ,1, 2)) 
