def staircase(n):
    n = int(input("enter a number:"))
    for i in range(1,n+1):
      print(('#'*i).rjust(n,' '))


staircase("n")