n, m= map(int,input().rstrip().split())
arr = list(map(int, input().rstrip().split()))
brr = list(map(int, input().rstrip().split()))

count = 0
for i in range(1,101):
    if all(i % j == 0 for j in arr) and all(j % i == 0 for j in brr):
        count += 1
print(count)
