import time
# ileride kullandığım time.sleep() için koydum
class Yolcu():    
    # Yolcu sınıfı oluşturdum her bir niteliği set get yaptım en sonda da printi tanımladım
   
    def __init__(self,adı,soyadı,cinsiyeti):
        # öznitelikleri tanımlarız
        self.adı=adı
        self.soyadı=soyadı
        self.cinsiyeti=cinsiyeti
        
    # özniteliklerin set get metodları
    def set_adı(self,adı):
        self.adı=adı
    def get_adı(self):
        return self.adı
    def set_soyadı(self,soyadı):
        self.soyadı=soyadı
    def get_soyadı(self):
        return self.soyadı
    
    def set_cinsiyeti(self):
        self.cinsiyeti
    def get_cinsiyeti(self):
        return self.cinsiyeti
    
    # printi tanımladım
    def __set__(self):
        return " "+ str(self.adı) + "   " + str(self.soyadı) +"   "+ str(self.cinsiyeti) +"  "


# In[0]:
# ========================
# Koltuk() sınıfı:
# Öznitelikler: int koltukNO, Boolean koltukDurum varsayılan False olsun, ve bir 
# Yolcu() yolcusu varsayılan None olsun
# Get/Set metotları (Bütün nitelikler için)
# get_yolcu ve set_yolcu() metotları tanımla, set_yolcu da koltuk durumunu değiştir.
# print metodu tanımla (Örnek: Koltuk no: 13, Mert Yılmaz, E)

class Koltuk():
      
    def __init__(self,koltukNO,koltukDurum=False,Yolcu=None):
       
       
       self.koltukNO=koltukNO
       self.koltukDurum=koltukDurum
       self.Yolcu=Yolcu
       
   
    
        
    # özniteliklerin set get metodları     
    def set_koltuk(self,koltukNO):
        self.koltukNO=koltukNO
        
    def get_koltuk(self):
        return self.koltukNO
    
    def set_koltuk_durumu(self,koltukDurum):
        self.koltukDurum=koltukDurum
        
    def get_koltuk_durumu(self):
        return self.koltukDurum
    
    def set_yolcu(self,Yolcu):
        self.set_koltuk_durumu(True)
        self.Yolcu=Yolcu
        
    def get_yolcu(self):
        return self.Yolcu
    
    # printi tanımladım
    def __str__(self):
       return  ""+ str(self.Yolcu.get_adı()) +""+ str(self.Yolcu.get_soyadı()) +""+ str(self.Yolcu.get_cinsiyeti()) +""

# In[0]:
# ========================
# Otobus() sınıfı özellikleri:
# Öznitelikler: str plaka, int KoltukSayısı varsayılan 42 olsun
# Her bir otobüs 42 koltuktan oluşacaktır, öncelike  self.koltukar = [] alıp
# Bu listeyi 42 boş koltukla doldurun (Koltuk() nesneleri ile)
# Get/Set metotları (Plaka ve koltuk sayısı nitelikleri için)


# koltukRezerv(y yolcusu, int koltukNo) metodu ile yolcu rezerve etsin, 
    # önceden rezerve edilmiş bir koltuk rezerve etmeye çalışırsanız
    # bir hata mesajı vermeniz gerekir, 
    # "rezerve edilmiş, koltukta ... kişi oturuyor" şeklinde.

# printYolcular() metodu bütün yolcuları yazdırsın. Örneğin,
    # Koltuk no: 13, Mert Yılmaz, E

 # printKoltuklar() metodu bütün koltukları yazdırsın. 
    # 1 False, None
    # ...
    # 13 True, Mert Yılmaz, E 
    # ...
    # gibi
    
# printBosKoltuklar() metodu bütün boş koltukların numarasını yazdırsın. "1 False, None" gibi

class Otobus():
    
    koltuklar=[] 
    # Boş bir koltuklar listesi oluşturduk
    
    def __init__(self,plaka,KoltukSayısı=42):
        # öznitelikleri tanımladık
        self.plaka=plaka
        self.KoltukSayısı=KoltukSayısı
      
        for i in range (1,43):
            # koltuklar listesini doldurmak iiçin gereken 42 sayı
            
            self.koltuklar.append(Koltuk(i)) 
            # koltuklar listesine 1 den 42 ye kadar (42 de dahil) numara atarız Koltuk() nesneleriyle
            
    # özniteliklerin set get metodları
    def set_plaka(self,plaka):
      self.plaka=plaka
      
    def get_plaka(self):
        return self.plaka
    
    def set_koltuk_sayısı(self,KoltukSayısı):
        self.KoltukSayısı=KoltukSayısı
        
    def get_koltuk_sayısı(self):
        return self.KoltukSayısı
    

    def KoltukRezerv(self,yolcusu,koltukNo):      
        # rezerve kısmını burada yapıyoruz
        
        if self.koltuklar[koltukNo].get_koltuk_durumu() == False:
            # eğer  koltuk durumu false ise kişiyi yerleştiriyoruz
            
            print("----- \n# Koltuk Rezerve İşlemi Tamamlandı")
            
            print("----- \n# Kayıt İşlemi Devam Ediyor Lütfen Bekleyiniz")
            
            time.sleep(1)
            # arada kısa bir süre bekleme,yükleme süresi eklemek istedim
            
            self.koltuklar[koltukNo].set_yolcu(yolcusu)
            
            print("----- \n# Kayıt İşlemi Tamamlandı İyi Yolculuklar")
            
        else:
            # false değil ise dolu uyarısı veriyor tekrar seçtiriyor
            print("----- \n# Koltuk DOLU! Lütfen Başka Bir Koltuk Seçiniz")
                
    def printYolcular(self):
        # tüm yolcuları görüntüleme de kullanılan kısım
        ü=0
        for i in self.koltuklar :
            # döngüye girdik koltuklar listesindeki elemanları tek tek i ye veriyor
            ü=ü+1
            if i.get_yolcu() is not None:
                
                # eğer i.get_yolcu() None değil ise kişiyi yazıyor 
                
               print("isim:{}, Soyisim:{}, Cinsiyeti:{}".format(i.get_yolcu().get_adı(),i.get_yolcu().get_soyadı(),i.get_yolcu().get_cinsiyeti()))
             
            else:
                # None ise...        
                print(ü,"-","\t\t\t\t[ --- ]")
                # boş olduğunu gösteririz.

    def printKoltuklar(self):
        # tüm koltukları görüntülemem kısmı
        for n in self.koltuklar:
            # koltuklar listesinde ki elemanları n ye tek tek veriyoruz
            a=""
            b=""
            # bu iki değer bizim koltuk durumu ve Yolcu durumunu belirtmemizi sağlar
            if n.get_koltuk_durumu() == False:
                # eğer n.get_koltuk_durumu() false ise a ve b değerleri yazılır
                a="Boş"
                b="Yok"
            else:
                # değil ise ...
                b=str((n.get_yolcu().get_adı(),n.get_yolcu().get_soyadı(),n.get_yolcu().get_cinsiyeti()))
                # b değerinde artık koltuğun dolduğunu ve kimin oturduğunu yazar
                a="Dolu"
                # a değeri de koltuğun dolu olduğunu belirtir
            print("KoltukNO:",n.get_koltuk(),"\tKoltukDurum:",a,"\tYolcu:",b)
    def printBosKoltuklar(self):
        # boş koltukları oluşturduğumuz kısım  burada
        
        for v in  self.koltuklar:
            # döngü yaptım koltuklar listesinde ki değerleri k ya atıyoruz
            
            if v.get_yolcu() is None:
                # eğer v.get_yolcu() None ise 
                
                print("Koltuk NO:"+str(v.get_koltuk()))         
    



# In[0]:
# ========================
# Bir main() metodu yazın
# Bir otobus örnek nesnesi oluşturun
# Menüyü göstersin, print ile ve
# Kullanıcının seçimine göre program kullanıcıdan parametre almalı ve ilgili
    # metotları çağırmalı.
# Örneğin, kullanıcı 1'girerse, yolcu adını, soyadını, cinsiyetini ve koltuk numarası
# alarak ilgili metodu çağırıp koltuk rezerve etsin. Menü'deki diğer rakamlar
# için de benzer işlemler yapmalı. İşlem 5'te çıkı ş için sys.exit kullanabilirsiniz.

# Programın menüsü şu şekilde olmalı
# ========================
"""
               MENU
        1- Rezervasyon yap
        2- Bütün yolcuları görüntüle
        3- Bütün koltukları görüntüle
        4- Bütün boş koltukları görüntüle
        5- Çıkış
        """

# Tercihinizi seçin:

   
def main():
    o=Otobus("28 GRU 454")
   
    print("""******************|ÇEKA TURİZME HOŞGELDİNİZ|******************
        """)
    print("\t\t\t\t\t  Plaka:",o.get_plaka())
    
    
    while True:
     
     try:  
        print("""\n----------------- MENU --------------------
              \n1-Rezervasyon
              \n2-Bütün Yolcuları Görüntülemek
              \n3-Bütün Koltuklar
              \n4-Bütün Boş Koltuklar
              \n5-Çıkış
              \n-------------------------------------------""")
              
        girdi=int(input("Yapmak İstediğiniz İşlemi Giriniz:"))
        try:
            assert girdi==str
            # girdi değeri sayısal bir değer olunca except bloğunda ki print çalışır
            # değil ise en aşşağıda ki except çalışır çünkü ana try da o var
            
        except:
            print("-----İŞLEMİNİZ-----")
        
        
        if girdi==1:
            # eğer 1 girerse yolcudan  input alma işlemi başlar
            
            kaçkişi=int(input("Kaç Kişi İçin Rezervasyon Yapılacak?:"))
            # rezervasyon edilecek kişi sayısı
            if kaçkişi>43:
                print("EN FAZLA 42 KOLTUK REZERVE EDİLEBİLİR")
                continue
            
        
            # kaç kişi için rezervasyon alınacağına kara verilen kısım
            if kaçkişi==1:
                # eğer 1 ise direkt 1 kişi alıp tekrar menuyü gösterir
                adı= input("Yolcu İsmi Giriniz:")
                
                soyadı= input("Yolcu Soyismi Giriniz:")

                cinsiyeti= input("Yolcu Cinsiyeti Giriniz (E\K):")

                yolcu= Yolcu(adı,soyadı,cinsiyeti)

                  
                koltukNO=input("KoltukNO:")
                # koltukNO 0 girilirse bu çalışacak
                if koltukNO=="0":
                    print("\nŞOFÖR KOLTUĞUNA REZERVASYON YAPILMAZ !!!")
                    continue
                # koltukNO 0 dan küçük(negatif) girilirse bu çalışacak
                if koltukNO<"0":
                    print("\nGİRDİĞİNİZ DEĞER NEGATİF BİR DEĞER,POZİTİF GİRİNİZ!")
                    continue
                # koltukNO 42 den büyük girilirse bu çalışacak
                if koltukNO>"42":
                    print("\nSADECE 42 KOLTUK VAR!!!")
                    continue
                # "" içinde olmazsa çalışmıyordu
                    
                o.KoltukRezerv(yolcu,int(koltukNO)-1)
                # 1 azaltmazsak mesela koltukNO=3 iken yolcu,4 çıktısı verir indexten dolayı
            else:
                i=0
                # i=0 dedim çünkü girilen sayı değerine kadar tekrar input aldırmam gerekiyor i de sürekli 1 artacak
                while kaçkişi>i:
                    # eğer kişi sayısı 1 den farklı ise girilen değer kadar input alırız
                    i=i+1
                    adı= input("Yolcu İsmi Giriniz:")
                    
                    soyadı= input("Yolcu Soyİsmi Giriniz:")
        
                    cinsiyeti= input("Yolcu Cinsiyet Giriniz:")
        
                    yolcu= Yolcu(adı,soyadı,cinsiyeti)
        
                      
                    koltukNO=input("KoltukNO:")
                        
                    o.KoltukRezerv(yolcu,int(koltukNO)-1)
                    # -1 demez isek koltukNO=3 girildiğinde 3ü değil 4 e ekler 0. indexi de sayarak
        elif girdi==2:
            o.printYolcular()
        #2 girerse program tüm yolcuları verir 
        if girdi==3:
            o.printKoltuklar()
        #3 girerse program tüm koltukları verir 
        elif girdi==4:
            o.printBosKoltuklar()
        #4 girerse program boş koltukları verir 
        if girdi==5:
            print("Yine Bekleriz :)")
            break
        # 5 girdiği anda programdan çıkar ve program durur
        elif girdi>5:
            print("\nListede Böyle Bir Sayı Yok Lütfen Tekrar Giriniz!")
            continue
        # 5 den büyük girerse alacağı mesaj
       
     except:
        
            print("\nLütfen Menüde ki Bir Seçeneği Seçiniz")
            # Eğer direkt sayı yazmazsak bu hata mesajı gelicek karşımıza
            
 

main()

    



              
   
    
    
    
    
   
