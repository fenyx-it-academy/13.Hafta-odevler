def staircase():
  n = int(input())
  # n icin veri girisi
  if 0 < n <= 100:
    # n ,0 ile 100 arasında ise
    for i in range(1, n):
      # 1 den n'e kadar dongu
      print(('#' * i).rjust(n))
        # n uzunlugunda satıra saga hizalı yıldız yazdırma
    print(('#' * n).rjust(n), end='')
      # alt satıra gecisi engellemek icin son satır end='' ile ayrı yazdırılıdı
staircase()
