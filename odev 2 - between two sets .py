arr = list(map(int, input().rstrip().split()))
brr = list(map(int, input().rstrip().split()))

list_first = []
list_result = []

for i in range(arr[-1],brr[0]+1):
    list_first += [i for x in arr if i%x==0]
    list_first += [i for y in brr if y%i==0]
list_result = set([i for i in list_first if list_first.count(i) == len(arr)+len(brr)])

print(len(list_result))

