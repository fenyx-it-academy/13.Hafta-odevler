def staircase(n):
    for i in range(1,n+1):
        value="#"*i
        print(value.rjust(n))
staircase(6)
