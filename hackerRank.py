#Staircase
#https://www.hackerrank.com/challenges/staircase/problem

def staircase(n):
  if 0 < n <= 100:
   for i in range(1,n+1):
       if i< n:
           print("\t".expandtabs((n-1)-i),'#'*i)
       else:
           print('#' * i)
  else:
    print("The number bigger than 100")
n = int(input("Please Enter a number for staircase: "))
staircase(n)

#Divisible Sum Pairs
#https://www.hackerrank.com/challenges/divisible-sum-pairs/problem
# !/bin/python3
# Complete the divisibleSumPairs function below.
def divisibleSumPairs(n, k, ar):
  divisible = 0
  for i in range(n):
    for j in range(i + 1, n):
      if (ar[i] + ar[j]) % k == 0:
        divisible += 1
  print(divisible)

nk = input().split()
n = int(nk[0])
k = int(nk[1])
ar = list(map(int, input().rstrip().split()))
result = divisibleSumPairs(n, k, ar)

#Between Two Sets
#https://www.hackerrank.com/challenges/between-two-sets/problem
def getTotalX(a, b):
  nList = [i for i in range(max(a), min(b) + 1)]
  cList = []
  cListLast = []
  for i in nList:
    for j in range(0, len(a)):
      if i % a[j] != 0:
        break
      elif i % a[j] == 0:
        if j == (len(a) - 1):
          cList.append(i)

  for i in cList:
    for j in range(len(b)):
      if b[j] % i != 0:
        break
      elif b[j] % i == 0:
        if j == (len(b) - 1):
          cListLast.append(i)
  return len(cListLast)


first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
m = int(first_multiple_input[1])
arr = list(map(int, input().rstrip().split()))
brr = list(map(int, input().rstrip().split()))
total = getTotalX(arr, brr)
print(total)