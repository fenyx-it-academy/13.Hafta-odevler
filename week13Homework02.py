def getTotalX(a, b):
    first_multiple_input = input("Please enter a and b :").rstrip().split()
    arr = list(map(int, input("Please enter the value of array a:").rstrip().split()))
    brr = list(map(int, input("please enter the value of array b: ").rstrip().split()))
    brr.sort()
    listt1=[]
    lisst2=[]
    for num in range(arr[-1],brr[0] + 1):
        for k in arr:
            if num % k!= 0:
                break
        else:
            lisst2.append(num)
    for b in lisst2:
        for num in brr:
            if num % b != 0:
                break
        else:
            listt1.append(b)
    print(lisst2)
    print((listt1))
    return len(listt1)


getTotalX(2, 3)

