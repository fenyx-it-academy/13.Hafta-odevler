def inputs():
    input1=int(input("Lutfen olusturacaginiz listenin elaman sayisini giriniz:"))
    input2=int(input("lutfen bolmek istediginiz sayiyi giriniz"))
    liste=[]
    for i in range(input1):
        number=int(input("Lutfen {} sayiyi giriniz").format(i+1))
        liste.append(number)
    liste.insert(0,input2)
    return liste
def check():
    liste=inputs()
    input2=liste[0]
    liste.remove(input2)
    liste1=[]
    k=1
    for i in range(len(liste)):
        l=k
        while i<l:
            try:
                liste1.append([liste[i],liste[l]])
            except IndexError:
                liste1.insert(0,input2)
                return liste1
            if l<(len(liste)-1):
                l+=1
                continue
            else:
                k+=1
                break
    liste1.insert(0,input2)
    return liste1
def consuquence():
    liste=check()
    print(liste)
    input2=liste[0]
    liste.remove(input2)
    counter=0
    for i in range(len(liste)):
        value=liste[i][0]+liste[i][1]
        if value%input2==0:
            counter+=1
    return print(counter)

consuquence()
