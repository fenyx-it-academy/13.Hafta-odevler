#ODEV1

n = int(input())
for i in range(n):
     print(("#"*(i+1)).rjust(n))

#ODEV2

first_multiple_input =input().rstrip().split()
arr = list(map(int, input().rstrip().split()))
brr = list(map(int, input().rstrip().split()))

liste=[i for i in range(max(arr),min(brr)+1) for j in arr if i%j==0]
b=[i for i in liste if liste.count(i)==int(first_multiple_input[0])]
liste2=[i for i in set(b) for j in brr if j%i==0]
c=[i for i in liste2 if liste2.count(i)==int(first_multiple_input[1])]

print(len(set(c)))

# ODEV3

nk = list(map(int, input().rstrip().split()))
ar = list(map(int, input().rstrip().split()))

print(len([[ar[i],ar[j]] for i in range(nk[0]) for j in range(nk[0]) if (ar[i]+ar[j])%nk[1]==0 and i<j]))

