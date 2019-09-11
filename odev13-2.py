##odev 2
first_multiple_input =input().rstrip().split()
arr = list(map(int, input().rstrip().split()))
brr = list(map(int, input().rstrip().split()))
liste=[]
for i in range(max(arr),min(brr)+1):
    for j in arr:
        if i%j==0:
            liste.append(i)
liste2=[]
for i in liste:
    if liste.count(i)==int(first_multiple_input[0]):
        liste2.append(i)
##        print(i)
liste3=[]
for i in range(max(arr),min(brr)+1):
    for j in brr:
        if j%i==0:
            liste3.append(i)
liste4=[]
for i in liste3:
    if liste3.count(i)==int(first_multiple_input[1]):
        liste4.append(i)
##        print(i)
liste2.extend(liste4)
##print(liste2)
sonl=[]
for i in liste2:
   if liste2.count(i)==int(first_multiple_input[0])+int(first_multiple_input[1]):
       sonl.append(i)
print(len(set(sonl)))
##2. yol kisaltilmis hali
##first_multiple_input =input().rstrip().split()
##arr = list(map(int, input().rstrip().split()))
##brr = list(map(int, input().rstrip().split()))
##liste=[i for i in range(max(arr),min(brr)+1)for j in arr if i%j==0 ]
##liste2=[i for i in liste if liste.count(i)==int(first_multiple_input[0])]
##liste3=[i for i in range(max(arr),min(brr)+1)for j in brr if j%i==0]
##liste4=[i for i in liste3 if liste3.count(i)==int(first_multiple_input[1])]
##liste2.extend(liste4)
##sonl=[]
##for i in liste2:
##   if liste2.count(i)==int(first_multiple_input[0])+int(first_multiple_input[1]):
##       sonl.append(i)
##print(len(set(sonl)))
