def staircase(f):
    for i in range(1, f + 1):
        print(('#'*i).rjust(f,' '))
n = int(input("Pleasa enter  a number: "))
staircase(n)
