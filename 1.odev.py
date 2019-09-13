print('b.')
'''
Boyutu n=4 olan bir merdiven düşünün:
#
##
###
####
Merdivenin hem başlangıcının hem de yüksekliğinin n’ye eşit olduğuna dikkat edin. Simge #
işareti ve boşluklar ile oluşturulmuştur. Son satırın başında boşluk bulunmamaktadır.
n boyutunda bir merdiven çıktısı veren bir program yazınız.
Merdiven örneği aşağıdaki parametrelere sahiptir:
n - integer
Input Formatı:
Merdivenin boyutunu belirten 1 adet n sayısı
Output Formatı:
# ve boşluk kullanarak n boyutunda bir merdiven çıktısı alın.
Not: Son satırda boşluk bulunmamalıdır.
Örnek Input
6
Örnek Output
     #
    ##
   ###
  ####
 #####
######
'''


def staircase(n):
    for i in range(1,n+1):
        print((i*'#').rjust(n,' '))
n = int(input('merdivenin boyutunu giriniz:'))
staircase(n)


