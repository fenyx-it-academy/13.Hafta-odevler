first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
m = int(first_multiple_input[1])
arr = list(map(int, input().rstrip().split()))
brr = list(map(int, input().rstrip().split()))

for i in range(arr,brr+1):
    x=0
    for a in arr:
        if  i % a == 0:
            x+=1
        if x == n:
            liste+= [i]
        else:
            
