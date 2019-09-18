def staircase(n):
    while True:
        if n<=0 or n>100:
            print('please number 1-100')
        for i in range(1,n+1):
            if i==n:
               print(('#'*i).rjust(n),end='')
            else:
                print(('#'*i).rjust(n))
        break
staircase(6)