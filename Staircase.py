n = int(input())
if n>0 and n<101:
    for i in range(n):
        print(("#"*(i+1)).rjust(n))
