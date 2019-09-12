def getTotalX(arr, brr):
    first_multiple_input = input("enter1:").rstrip().split()

    n = int(first_multiple_input[0])
    m = int(first_multiple_input[1])
    arr = list(map(int, input("enter arr:").rstrip().split()))
    brr = list(map(int, input("enter brr:").rstrip().split()))

    bolen = []
    for i in brr:
        for j in range(1,i):
            for a in range(m):
                if brr[a]%j ==0 :
                    bolen.append(j)

    return print(len([max(bolen),max(arr)]))
getTotalX("arr","brr")

if __name__ == '__main__':
    fptr = open("liste.txt", 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()