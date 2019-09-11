def staircase(n):
    a='#'
    c=1
    for i in range(n):
        print((a*c).rjust(n," "))
        c+=1
n = int(input("Kac basamakli bir merdiven istersiniz:"))
staircase(n)