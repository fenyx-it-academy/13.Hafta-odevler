n=int(input('lutfen sayi giriniz'))
for i in range(n+1):
    if i==n:
        print('#'*i)
    else:
        print("\t".expandtabs (( n-1)-i ),'#'*i)
