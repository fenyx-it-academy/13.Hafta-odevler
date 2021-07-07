
x=0
y=[]
n = int(input("Entre one number betwen 1-100 : "))
while True :
    if n != x :
        x += 1
        y += [x]
    else:
        break
for i in y:
    print(str('#'*i).rjust(n,' '))



