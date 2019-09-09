def staircase(n):
    m = 1
    while n > 0:
        print((n-1)*' ' + m*'#')
        n -= 1
        m += 1
while True:
    n = int(input())
    if n<1 or n>100:
        continue
    else:
        staircase(n)
        break
