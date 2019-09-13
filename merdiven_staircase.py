def stairs(n):
    for a in range(1, n + 1):
        print(" " * (n - a) + "#" * a)
                
if __name__ == '__main__':
    n = int(input())
    if 0<n<=100:
        stairs(n)