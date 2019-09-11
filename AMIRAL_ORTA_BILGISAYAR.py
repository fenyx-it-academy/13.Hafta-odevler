import random
import time as zaman
#*******************OYUN TABLOSU CLASS I  TAHTA HAZIRLAMA*********************************
class amiral_oyun_tablosu():
    def __init__(self):
        self.sanal_tahta = [["---" for b in range ( 10 )] for a in range ( 10 )]
        self.koordinat_x_y = [(a , b) for b in range ( 10 ) for a in range ( 10 )]
        self.depo = []
        self.torba = []
        self.gemi_yatay = []
        self.gemi_dikey = []
        self.kaclik_gemi = []
        self.sayac=0
        self.gemicik=[5,4,4,3,3,2,2,1,1]
#********************************************************************************
    def gemi_hazirlama(self): #GEMICIK ICERISINDEKI GEMILERI YAPMA
        self.gemi=self.gemicik[self.sayac]
        self.sayac+=1
        if self.sayac==len(self.gemicik):
            self.sayac=0
        self.sec = random.randint ( 0 , 1 )  #DIKEY YATAY OLMA DURUMUNU AYARLAYAN RANDOM
        if self.sec == 0 :
            self.gemi_yatay = [[(a , b + c) for b in range ( self.gemi )] for a in range ( 10 ) for c in
                          range ( 10 - self.gemi + 1 )]
            return self.gemi_yatay
        if self.sec == 1 :
            self.gemi_dikey = [[(b + c , a) for b in range ( self.gemi )] for a in range ( 10 ) for c in
                          range ( 10 - self.gemi + 1 )]
            return self.gemi_dikey
#************************************************************************************
    #BU FONKSIYON GEMILER BIRBIRINE DEGMESIN DIYE CEVRESINI BOSALTIR
    def temizle(self,secime_git): #X DEGERLERININ CEVRESINI BOSALTAN FONKSIYON
        silme = []
        asagi_sil = [[((a + 1) % 10 , b) for b in range ( 10 )] for a in range ( 10 )]
        yukari_sil = [[((a + 9) % 10 , b) for b in range ( 10 )] for a in range ( 10 )]
        sag_sil = [[(a , b + 1) for b in range ( 10 )] for a in range ( 10 )]
        sol_sil = [[(a , b - 1) for b in range ( 10 )] for a in range ( 10 )]
        for i in secime_git :
            if 0 < i[0] < 9 and i in self.koordinat_x_y :
                silme += [asagi_sil[i[0]][i[1]]]
                silme += [yukari_sil[i[0]][i[1]]]
            if 0 < i[1] < 9 and i in self.koordinat_x_y :
                silme += [sag_sil[i[0]][i[1]]]
                silme += [sol_sil[i[0]][i[1]]]
            if i[0] == 0 and i in self.koordinat_x_y :
                silme += [asagi_sil[i[0]][i[1]]]
            if i[0] == 9 and i in self.koordinat_x_y :
                silme += [yukari_sil[i[0]][i[1]]]
            if i[1] == 0 and i in self.koordinat_x_y :
                silme += [sag_sil[i[0]][i[1]]]
            if i[1] == 9 and i in self.koordinat_x_y :
                silme += [sol_sil[i[0]][i[1]]]
        silme.extend ( secime_git )
        for i in set ( silme ) :
            if i in self.koordinat_x_y :
                self.koordinat_x_y.remove ( i )
        return
#********************************************************************************
    def ekrana_yaz(self) :
        for i in self.depo :
            self.kaclik_gemi += [len ( i )]
            if len(i)==5:
                for yaz in i :
                    self.sanal_tahta[yaz[0]][yaz[1]] = ('5').center ( 3 )
            if len(i)==4:
                for yaz in i :
                    self.sanal_tahta[yaz[0]][yaz[1]] = ('4').center ( 3 )
            elif len ( i ) == 3 :
                for yaz in i :
                    self.sanal_tahta[yaz[0]][yaz[1]] = ('3').center ( 3 )
            elif len ( i ) == 2 :
                for yaz in i :
                    self.sanal_tahta[yaz[0]][yaz[1]] = ('2').center ( 3 )
            elif len ( i ) == 1 :
                for yaz in i :
                    self.sanal_tahta[yaz[0]][yaz[1]] = ('1').center ( 3 )
    def ekrani_goster(self):
        print('\n'*3)
        for i in self.sanal_tahta :
            print ( ' ' * 40 , *i , '\n' )

#***************************************************************************
    def gemi_tablo(self):
        gemiadeti = 0
        while gemiadeti < len(self.gemicik) :
            self.gemi_hazirlama()
            for i in self.gemi_hazirlama () :
                if set ( i ).issubset ( set ( self.koordinat_x_y ) ) :  # tahtanin icinde alt kume olarak varmi
                    self.torba += [i]
            if self.torba != [] :
                secime_git = random.choice ( self.torba )
            self.torba = []
            self.depo.append ( secime_git )
            self.temizle ( secime_git )
            gemiadeti += 1
# ****************************************************************************************
oyuncu_tablo=amiral_oyun_tablosu()  #BILGISAYARA AIT GEMI EKRANI CLASI
oyuncu_tablo.gemi_tablo()           #BILGISAYR EKRANI ICIN GEMI HAZIRLAMA
oyuncu_tablo.ekrana_yaz()           #GEMILERI YUKLEME
# oyuncu_tablo.ekrani_goster() #ILK ACILISTA BILGISAYAR GEMILERINI GOSTERMEK ISTENIRSE
#**************************************************************************8
#OYUNCUYA AIT GEMI EKRANI CLASI
bilgisayar_tablo=amiral_oyun_tablosu()
bilgisayar_tablo.gemi_tablo() #OYUNCU EKRANI GEMI HAZIRLAMA
bilgisayar_tablo.ekrana_yaz() #OYUNCU EKRANI GEMI HAZIRLAMA

#*******************OYUN  CLASS I *********************************
class Amiral_Oyuncu():
    def __init__(self):
        self.bos = []
        self.tam_isabet = []
        self.tahta = [["---" for b in range ( 10 )] for a in range ( 10 )]
        self.atis_kontrol = [' 1 ' , ' 2 ' , ' 3 ' , ' 4 ' , ' 5 ' , '<~>']
        self.isabet_gemi = [' 1 ' , ' 2 ' , ' 3 ' , ' 4 ' , ' 5 ']
#*************************************************************************
    def hata(self , hata) :
        iska = list ( hata )
        if self.tahta[int ( hata[0] )][int ( hata[1] )] in self.atis_kontrol :
            print ( 'Hey... iyimisin buraya daha once ates ettin' )
            return 'hata'
 #**************************************************************************
    def hedef(self,nisan) :
        isabet = list ( nisan )
        if bilgisayar_tablo.sanal_tahta[int ( isabet[0] )][int ( isabet[1] )] in self.isabet_gemi :
            self.tam_isabet = [isabet]
            return self.tam_isabet
# ****************************************************************************************
    #                       BOS ATISLAR ICIN FONKSIYON
    def iska(self,bosa) :
        iska = list ( bosa )
        if bilgisayar_tablo.sanal_tahta[int ( iska[0] )][int ( iska[1] )] == ('---').center ( 3 ) :
            self.bos = [iska]
        return self.bos  # bos listesi fonksiyonun cagirildigi yere dondurulur

# ****************************************************************************************
    def ust_ekran(self):

        print ( ' ' * 5 , 'OYUNCUNUN  ATIS SIRASI ' )
#**********************************************************************************************
    def ekran(self) :
        print ( ' ' * 60 , 'BILGISAYAR EKRANI' )  # hamle sayisi gosterme
        print ( '\n' , ' ' * 36 , ' [Y] -->   [{}] [{}] [{}] [{}] [{}] [{}] [{}] [{}] [{}] [{}]'.
                format ( 0 , 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 ) , '\n' )
        sayac = 0
        for i in self.tahta :
            print ( ' ' * 38 , '[X][' , sayac , '] ' , *i , '\n' )
            sayac += 1
#*******************OYUN  CLASS I*********************************
class Amiral_Bilgisayar():
    def __init__(self):
        self.bos = []
        self.tam_isabet = []
        self.tahta = [["---" for b in range ( 10 )] for a in range ( 10 )]
        self.atis_kontrol = [' X ' , '<~>']
        self.isabet_gemi = [' 1 ' , ' 2 ' , ' 3 ' , ' 4 ' , ' 5 ']
        self.sayi=[(a,b) for b in range ( 10 ) for a in range ( 10 )]
        self.atis_kutu=[]
        self.silme = []
        self.tarama=[]
#*************************************************************************
    def oyuncu_tahta_hazirla(self) :
        for i in oyuncu_tablo.depo :
            oyuncu_tablo.kaclik_gemi += [len ( i )]
            if len ( i ) == 5 :
                for yaz in i :
                     self.tahta[yaz[0]][yaz[1]] = ('5').center ( 3 )
            if len ( i ) == 4 :
                for yaz in i :
                    self.tahta[yaz[0]][yaz[1]] = ('4').center ( 3 )
            elif len ( i ) == 3 :
                for yaz in i :
                    self.tahta[yaz[0]][yaz[1]] = ('3').center ( 3 )
            elif len ( i ) == 2 :
                for yaz in i :
                    self.tahta[yaz[0]][yaz[1]] = ('2').center ( 3 )
            elif len ( i ) == 1 :
                for yaz in i :
                    self.tahta[yaz[0]][yaz[1]] = ('1').center ( 3 )
    #**************************************************************8
    #BU KISIMDA GEMIYI ILK VURDUGUNDA DIGER PARCASINI BULMAK ICIN CEVRESINI TARAMA YERI
    def atis_hazirlik(self,ates):
        yukari_sil = [[((a + 9) % 10 , b) for b in range ( 10 )] for a in range ( 10 )]
        asagi_sil = [[((a + 1) % 10 , b) for b in range ( 10 )] for a in range ( 10 )]
        sag_sil = [[(a , b + 1) for b in range ( 10 )] for a in range ( 10 )]
        sol_sil = [[(a , b - 1) for b in range ( 10 )] for a in range ( 10 )]
        if oyuncu_tablo.sanal_tahta[int ( ates[0] )][int ( ates[1] )] in self.isabet_gemi and self.silme==[]:
            for i in oyuncu_tablo.depo:
                if ates in i:
                    self.silme+=i

                    if 0 < ates[0] < 9 and ates in self.sayi :
                        self.tarama += [asagi_sil[ates[0]][ates[1]]]
                        self.tarama += [yukari_sil[ates[0]][ates[1]]]
                    if 0 < ates[1] < 9 and ates in self.sayi :
                        self.tarama += [sag_sil[ates[0]][ates[1]]]
                        self.tarama += [sol_sil[ates[0]][ates[1]]]

                    if  ates[0]==0  and ates in self.sayi :
                        self.tarama += [asagi_sil[ates[0]][ates[1]]]
                    if ates[0] == 9 and ates in self.sayi :
                        self.tarama += [yukari_sil[ates[0]][ates[1]]]
                    if  ates[1]==0  and ates in self.sayi :
                        self.tarama += [sag_sil[ates[0]][ates[1]]]
                    if ates[1] == 9 and ates in self.sayi :
                        self.tarama += [sol_sil[ates[0]][ates[1]]]

                    self.silme=set(self.silme )
                    self.silme=list(self.silme )
                    return
        else:
            return ates

#*************************************************************8
    #BU KISIM ILK RANDOM ATESLEME YAPMAK ICIN VURUNCA YUKARIDAKI FONKSIYON CALISIYOR
    def atis(self):
        c = random.choice ( self.sayi )
        self.atis_hazirlik ( c)
        if c in self.atis_kutu:
            return c
        else:
            self.atis_kutu.append(c)
            self.sayi.remove(c)
            return c
#************************************************************************
    #AYNI YERE ATISLARI KONTROL EDIYOR
    def hata(self , hata) :
        if self.tahta[int ( hata[0] )][int ( hata[1] )] in self.atis_kontrol :
            print ( 'Hey... iyimisin buraya daha once ates ettin' )
            return 'hata'
#****************************************************************************
    # ISABET EDEN KISIMLARI KONTROL EDIYOR
    def hedef(self,isabet) :
        if oyuncu_tablo.sanal_tahta[int ( isabet[0] )][int ( isabet[1] )] in self.isabet_gemi :
            self.tam_isabet = [isabet]
            return self.tam_isabet
# ****************************************************************************************
    #BOSA ATISLARI KONTROL EDIYOR
    def iska(self , iska) :
        if oyuncu_tablo.sanal_tahta[int ( iska[0] )][int ( iska[1] )] == ('---').center ( 3 ) :
            self.bos = [iska]
            return self.bos  # bos listesi fonksiyonun cagirildigi yere dondurulur
# ****************************************************************************************
    def ust_ekran(self) :
        print ( ' ' * 5 , 'BILGISAYARIN  ATIS SIRASI ' )
#***********************************************************************************
    def ekran(self) :
        print ( ' ' * 60 , 'OYUNCU EKRANI' )  # hamle sayisi gosterme

        print ( '\n' , ' ' * 36 , ' [Y] -->   [{}] [{}] [{}] [{}] [{}] [{}] [{}] [{}] [{}] [{}]'.
                format ( 0 , 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 ) , '\n' )
        sayac = 0
        for i in self.tahta :
            print ( ' ' * 38 , '[X][' , sayac , '] ' , *i , '\n' )
            sayac += 1
# ****************************************************************************************
oyuncu=Amiral_Oyuncu()

bilgisayar=Amiral_Bilgisayar()
bilgisayar.oyuncu_tahta_hazirla()
print ( """

************************************************************************************************
                            AMIRAL BATTI
             Deniz olarak varsayacagimiz 10x10'luk bir tablomuz var.
           Bu tabloda

                          1 adet 5 birimlik 5
                          2 adet 4 birimlik 4
                          2 adet 3 birimlik 3
                          2 adet 2 birimlik 2
                          2 adet 1 birimlik 1

           gemiler mevuttur.Bu gemiler x ve y ekseni dogrultusunda olabilir.
           Sizden istenilen tablo uzerindeki herhangi bir noktaya hamlede bulunun
           ve gemileri vurmaya calisin.Gemilerin herhangi bir noktasina isabet ederse
           ekranda bunu '' 5 ',' 4 ',' 3 ',' 2 ' ,,' 1 'goreceksin.Ayni sekilde bosa atis yaptiginda da <~>
           goreceksin.Her atis oncesi 3 saniye beklemelisin.Daha once yapmis oldugun
           hamleler icin uyari alacaksin.
           Eger tum gemileri vurursan oyunu kazanirsin.
           Atis konumu  x,y koordinat duzeni seklindedir.[x][y],05 gibi bir deger girersen
           x=0,y=5 seklinde konumlandirir.

************************************************************************************************
simdi oyununuz basliyor...............................................
""" , '\n' * 3 )
#***********OYUN BASLAMA********************8
while True :
    # ***********************************************************************
    #      INPUT ALMA VE HATALARI DUZELTME
    oyuncu.ust_ekran ()
    oyuncu.ekran ()
    oku = input ( '\n'"""Konum  xy (01) giriniz,
    [cikis=Q]--> :""" )
    if oku.upper () == 'Q' :
        print ( 'oyundan cikiliyor............' )
        zaman.sleep ( 2 )
        break
    elif oku.isdigit () == False or len ( oku ) != 2 :
        print ( 'lutfen x ve y degerini xy (93) seklinde giriniz' )
        continue
    if oyuncu.hata ( oku ) == 'hata' :
        continue
    elif oyuncu.hedef ( oku ) == oyuncu.tam_isabet :
        for x in oyuncu.tam_isabet :
            oyuncu.tahta[int ( x[0] )][int ( x[1] )] = bilgisayar_tablo.sanal_tahta[int ( x[0] )][int ( x[1] )]
            print ( 'bravo hedefi 12 den vurdun ' )
        if sum ( [oge.count ( ' X ' ) for satirlar in oyuncu.tahta for oge in satirlar] ) == 25 :
            print ( """OYUNCU KAZANDI """ )
            zaman.sleep ( 2 )
            quit ()
        continue
    elif oyuncu.iska ( oku ) == oyuncu.bos :
        for i in oyuncu.bos :
            oyuncu.tahta[int ( i[0] )][int ( i[1] )] = '<~>'.center ( 3 )
        print ( 'ne yazik ki iska gectin..' )
        oyuncu.ekran ()
        zaman.sleep ( 2 )
        bilgisayar.ust_ekran ()
        bilgisayar.ekran ()
        dongu=2
    while dongu==2:
        if bilgisayar.silme!=[]:

            if bilgisayar.tarama!=[] :
                z=random.choice(bilgisayar.tarama)
                bilgisayar.tarama.remove(z)
                if z in bilgisayar.atis_kutu:
                    continue
                else:
                    bilgisayar.atis_kutu.append ( z )
                    bilgisayar.sayi.remove ( z )


                if oyuncu_tablo.sanal_tahta[int ( z[0] )][int ( z[1] )] in bilgisayar.isabet_gemi :
                    bilgisayar.tarama.clear()

            else:

                z=random.choice(bilgisayar.silme)
                bilgisayar.silme.remove ( z )
                if z in bilgisayar.atis_kutu:
                    continue
                else:
                    bilgisayar.atis_kutu.append ( z )
                    bilgisayar.sayi.remove ( z )
        else:
            z = bilgisayar.atis ()
        print(z)
        zaman.sleep ( 2 )
        if bilgisayar.hata ( z ) == 'hata' :
            continue
        elif bilgisayar.hedef ( z ) == bilgisayar.tam_isabet :
            for x in bilgisayar.tam_isabet :
                bilgisayar.tahta[int ( x[0] )][int ( x[1] )] = 'X'.center ( 3 )
                print ( 'bravo hedefi 12 den vurdun ' )
                bilgisayar.ekran ()
                zaman.sleep ( 3 )
            if sum ( [oge.count ( ' X ' ) for satirlar in bilgisayar.tahta for oge in satirlar] ) == 25 :
                print ( """BILGISAYAR KAZANDI """ )
                zaman.sleep ( 2 )
                quit ()
            continue
        elif bilgisayar.iska ( z ) == bilgisayar.bos :
            for i in bilgisayar.bos :
                bilgisayar.tahta[int ( i[0] )][int ( i[1] )] = '<~>'.center ( 3 )
            print ( 'ne yazik ki iska gectin..' )
            bilgisayar.ekran ()
            zaman.sleep ( 3 )
            break
    continue