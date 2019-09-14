# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 19:51:05 2019

@author: HP
"""
# Between Two Sets

# Program ;You will be given two arrays of integers and asked to determine all integers that satisfy 
#the following two conditions:

# 1-The elements of the first array are all factors of the integer being considered
# 2-The integer being considered is a factor of all elements of the second array

#These numbers are referred to as being between the two arrays. You must determine how many such numbers exist.

def getTotalX(a,b):   
    bolen=[] ; bolenler=[]
    
    for x in range(max(a),min(b)+1):
        control = 0
        for j in range(len(a)):
            if x%a[j]!=0:
                control=1
                break
            else:
                control=0
        if control==0:
                bolen.append(x)
    
    for y in bolen:
        kontrol=0
        for k in range(len(b)):
            if b[k]%y!=0:
                kontrol=1
                break
        if kontrol==0:
            bolenler.append(y)      
    
    print('\nIki liste arasi sayilar;',*bolenler) 
    print(f'Toplam iki liste arasi sayilar {len(bolenler)} adettir')       
       
    
if __name__== '__main__':
    first_multiple_input = input("Iki Listenin eleman sayilarini birer bosluk birakarak giriniz ;").rstrip().split()
    n = int(first_multiple_input[0])
    m = int(first_multiple_input[1])
    print(f'\n{n} elemanli ilk listenizin elemanlarini giriniz')
    arr = list(map(int, input("Elemanlari birer bosluk birakarak giriniz ;").rstrip().split()))
    print(f'\n{m} elemanli ikinci listenizin elemanlarini giriniz')
    brr = list(map(int, input("Elemanlari birer bosluk birakarak giriniz ;").rstrip().split()))
    getTotalX(arr, brr)
    
    
# =============================================================================
# Benim liste girisim...
# a=[] ; b=[] 
# giris=input("Iki Listenin eleman sayilarini birer bosluk birakarak giriniz ;")
# gir=giris.split()
# n=int(gir[0])  
# m=int(gir[1])
# 
# print(f'\n{n} elemanli ilk listenizin elemanlarini giriniz')
# veri1=input("Elemanlari birer bosluk birakarak giriniz ;)
# a=veri1.split()
# a=[int(i) for i in a]
# if len(a)==n:        
#     print("\nIlk listeniz;",*a)
# else:
#     print('Lutfen eleman sayisina dikkat ediniz...')
# 
# print(f'\n{m} elemanli ikinci listenizin elemanlarini giriniz')
# veri2=input("Elemanlari birer bosluk birakarak giriniz ;")
# b=veri2.split()
# b=[int(i) for i in b]
# b.sort()
# if len(b)==m:        
#     print("\nIkinci listeniz;",*b)
# else:
#     print('Lutfen eleman sayisina dikkat ediniz...')      
# =============================================================================

