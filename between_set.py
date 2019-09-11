# a=[2 ,4]
# b=[16,32,96]
# e=[i for i in range(a[-1],b[0]+1) for z in range(len(b)) if b[z]%i==0]
# f=[i for i in range(a[-1],b[0]+1) for z in range(len(a)) if i%a[z]==0]
# e.extend(f)
# s=[i for i in e if e.count(i)>=len(b)+len(a)]
# s=set(s)
# print(len(s))

def getTotalX(a, b):
    e=[i for i in range(a[-1],b[0]+1) for z in range(len(b)) if b[z]%i==0]
    f=[i for i in range(a[-1],b[0]+1) for z in range(len(a)) if i%a[z]==0]
    e.extend(f)
    s=[i for i in e if e.count(i)>=len(b)+len(a)]
    s=set(s)
    print(len(s))  

first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
m = int(first_multiple_input[1])
arr = list(map(int, input().rstrip().split()))
brr = list(map(int, input().rstrip().split()))
total = getTotalX(arr, brr)



#BETWEEN TWO SETS
#a=[2 ,4]
#b=[16,32,96]
# 2 den 16 ya kadar olan bolenler
# 4 den 16 ya kadar olan bolenler bulunacak bir listeye atin
#bu bolenlerden BURASINA DIKKAT 2 ve 4 de tam bolunecek i%2=0 ve i%4=0 degerleri secilecek
#sonra buldugunuz tam bolunen degerlerini b listesindeki degerlere boldureceksiniz yani b[liste]%i=0
#degerleri bulunacak bir listeye atin
#BURADA ANLASILMASI ZOR BIR MESELE VAR ISTENEN DEGERLER(SAYIMIZ X OLSUN)
#HEM 2,4 ILE KALANSIZ BOLECEK X%4 VE X%2 =0
#HEMDE B LISTESINDEKI SAYILARA KALANSIZ BOLUNECEK 16%X 32%X 96%X =0
#BU SARTLARI SAGLAYAN DEGERLER ISTENIYOR
