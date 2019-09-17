def getTotalX(a, b):
    dividens_a=[]
    dividens_b=[]
    for i in range (max(a),min(b)+1):
        for k in range(0,len(a)):
            if i%a[k]!=0:
                break
        else:
            dividens_a.append(i)
    for i in dividens_a:
        for k in b:
            if k%i!=0:
                break
        else:
            dividens_b.append(i)
    return len(dividens_b)
#first_multiple_input = input().rstrip().split()
#n = int(first_multiple_input[0])
#m = int(first_multiple_input[1])
#arr = list(map(int, input().rstrip().split()))
#brr = list(map(int, input().rstrip().split()))
arr=[2,4]
brr=[16,32,96]
total = getTotalX(arr, brr)
print(total)
