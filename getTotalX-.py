def getTotalX(a, b):
  a.sort()
  b.sort()
  # a ve b listelerinin elemanlarını sırala
  x=len(a)
  y=len(b)
  # a ve b listelerinin elemanları uzunluklarını degiskenlere ata
  lcm=set()
  gcd=set()
  # lcm ve gcd bos kumeleri tanımla
  for i in range(a[x-1],b[0]+1):
    # a listesinin en buyuk elemanından b nin en kucuk elemanı arasında dongu
    for j in range(x):
      # a listesi uzunlugunca dongu
      if i%a[j]!=0:
        # i, a listesinin herbir elemenına bolunebilme duruumunu kontrol
        break
        # bolunmeme durumu varsa ilk donguden cık
    else:
      lcm.add(i)
      # herbir eleman ile bolunuyora lcm listesine i yi ekle
  for i in range(a[x-1],b[0]+1):
    for j in range(y):
      if b[j]%i!=0:
        break
    else:
      gcd.add(i)
  print(len(lcm&gcd))
  # lcm ve gcd listelerinin kesisimini al ve yazdır
first_multiple_input = input().rstrip().split()
# veri girisi
n = int(first_multiple_input[0])
# girilen str'nin 0 indisli elemnını int yap n'e ata
m = int(first_multiple_input[1])
# girilen str'nin 1 indisli elemnını int yap m'e ata
arr = list(map(int, input().rstrip().split()))
# arr listesini olustur
brr = list(map(int, input().rstrip().split()))
# brr listesini olustur
total = getTotalX(arr, brr)

