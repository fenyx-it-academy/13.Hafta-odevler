##2.Odev
##Verilen iki listeden ilk listenin tüm elemanlarının tam bölebildiği bir
##sayıların, ikinci listenin tüm elemanlarını tam bölebildiği durumların
##sayısını tespit eden bir fonksiyon yazınız. Bu tür sayılara iki liste
##arası sayılar diyeceğiz. Bu tür sayıların sayısını tespit etmeniz gerekmektedir.

a=[2,4]
b=[16,32,96]

c=a+b
d=sorted(c)
aa=[]
bb=[]
for i in range(d[0],d[len(d)-1]):
    if i % a[0] == 0 and i % a[1] == 0 and i not in aa:
            aa+=[i]
for t in aa:
    if b[0] % t == 0 and b[1] % t == 0 and b[2] % t == 0 and t not in bb:
        bb+=[t]

print('iki liste arası sayılar listesi : ',bb)
print('iki liste arası: ',len (bb),'adet sayi var')
