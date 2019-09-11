## ODEV 1
def staircase(n):   
    Bosluk = 1*n - 1
    for i in range(0, n): 
        for j in range(Bosluk): 
            print(end=" ") 
        Bosluk = Bosluk - 1
        for j in range(0, i+1): 
            print("#", end="") 
        print("\r") 
n =int(input("bir"))
staircase(n)
