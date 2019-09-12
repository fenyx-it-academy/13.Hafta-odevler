

#1 Staircase

n = int(input())
for i in range(1, n+1):
        print(" " * (n - i) + "#" * i)


#2 Between Two Sets

first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
m = int(first_multiple_input[1])
arr = list(map(int, input().rstrip().split()))
brr = list(map(int, input().rstrip().split()))
yeni = []
sonuc = []
for i in range(max(arr), min(brr) + 1):
    y=0
    
    for a in arr:
        if i % a == 0:
            y += 1
        if y==n:
            yeni+=[i]
        else:
            continue

for y in yeni:
    k=0
    for b in brr:
        if b % y == 0:
            k+=1
        if k==m:
            sonuc += [y]
        else:
            continue

print(len(sonuc))



# 3 Divisible Sum Pairs

sonuc=0
for x in range(n):
    for y in range(n):
        if x < y and (ar[x] + ar[y]) % k == 0:  # ilk index ikinci indexten kucukse ve toplamlari k sayisi ile bolunebiliyorsa sonucu 1 artiriyor 
            sonuc+=1
        else:
            continue
print(sonuc)

# kisa yolu
son=[1 for x in range(n) for y in range(n) if x < y and (ar[x] + ar[y]) % k == 0]   # uretecli hali 
print(len(son))