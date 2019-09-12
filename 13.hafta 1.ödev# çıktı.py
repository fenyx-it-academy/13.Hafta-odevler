def staircase(n):
    for i in range(1,n+1):
        print(" "*(n-i),"#"*i,sep="",end="")
        if i<n:
            print("\n",sep="",end="")
if __name__ == '__main__':
    n = int(input())
    if 0<n<101:
        staircase(n)
