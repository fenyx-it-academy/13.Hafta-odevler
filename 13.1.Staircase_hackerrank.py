print(14 * " >", "\t n.B.a. \t", "< " * 14, "\n\n\n")


def staircase(n):
    for v in range(1, n+1):
        print((n-v) * ' ' + v * '#')                # '#' eklendikten sonra geri kalan bosluk olsun


n = int(input())
staircase(n)
