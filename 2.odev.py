##2.Odev
##Verilen iki listeden ilk listenin tüm elemanlarının tam bölebildiği bir
##sayıların, ikinci listenin tüm elemanlarını tam bölebildiği durumların
##sayısını tespit eden bir fonksiyon yazınız. Bu tür sayılara iki liste
##arası sayılar diyeceğiz. Bu tür sayıların sayısını tespit etmeniz gerekmektedir.

def getTotalX(a, b):
    sayac=0
    for i in range(max(arr),min(brr)+1):
        lista=[i%x for x in arr]  
        liste=[x%i for x in brr] 
        if lista.count(0)+liste.count(0)==n+m: 
            sayac+=1                    
    return sayac
first_multiple_input = input("Enter two numbers for the length of your lists:").rstrip().split()
n = int(first_multiple_input[0])
m = int(first_multiple_input[1])
arr = list(map(int, input("elements of your first list").rstrip().split()))
brr = list(map(int, input("elements of your last list:").rstrip().split()))
total = getTotalX(arr, brr)
print(total)
