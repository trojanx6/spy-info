import os
try:
    from urllib.request import urlopen
except ModuleNotFoundError:
    os.system("pip3 install urllib")
    os.system("pip3 install request")
    
    
print("""

   \  <>      Spy İnfo     <>  /
           
<v.1>
[+] TERS  DNS araması 1
[+] ANA Bilgiseyar kayıtları 2
[+] DNS araması 3
[+] PAYLAŞILAN DNS Sunucuları 4
[+] SİTE linkleri çıkarma 5
[+] HTTP başlıklarından bilgi alma 6
[+] OTONOM sistemi arama 7
[+] İP adresinden konum bulma 8
[+] ZONE Transfer 9

coder by: https://github.com/trojanx6

""")


islem = int(input("işlem giriniz: "))

    
hata_mesaji = 'Hata oldu lütfen tekrar deneyiniz'
    
    
    
    
    
    
    
def reversedns():
    try:
        hedef = input("Hedef Dns adresi(8.8.8.8): ")
        url = ("https://api.hackertarget.com/reversedns/?q="  + hedef)
        reverse = urlopen(url).read()
        sonuc = reverse.decode('UTF-8')
        print(sonuc)
        
    except:
        print(hata_mesaji)




def search():
    try:
        hedef = input("alan adı gir (alt alan icin): ")
        url = ("https://api.hackertarget.com/hostsearch/?q=" +  hedef)
        domain = urlopen(url).read()
        sonuc = domain.decode('UTF-8')
        print(sonuc)
        
    except:
        print(hata_mesaji)




def dns():
    try:
        hedef =  input("Hedef İp&Domain: ")
        url = ("http://api.hackertarget.com/dnslookup?q=" + hedef)
        dns_kayit = urlopen(url).read()
        sonuc = dns_kayit.decode('UTF-8')
        print(sonuc)
        
    except:
        print(hata_mesaji)
                            
                            
                            
                            
def zone():
    try:
        hedef = input("hedef domain adı: ")
        url = ("https://api.hackertarget.com/findshareddns/?q=" + hedef)
        zone = urlopen(url).read()
        sonuc = zone.decode('UTF-8')
        print(sonuc)
        
    except:
        print(hata_mesaji)
                                     
                                     
                                     
def link():
    try:
        hedef = input("hedef site gir: ")
        url = ("https://api.hackertarget.com/pagelinks/?q=" + hedef)
        link = urlopen(url).read()
        sonuc = link.decode('UTF-8')
        print(sonuc)
        
    except:
        print(hata_mesaji)
                                
                                
                                
def asm():
    try:
        hedef = input("dns giriniz: ")
        
        url = ("https://api.hackertarget.com/aslookup/?q=" + hedef)
        asm = urlopen(url).read()
        sonuc = asm.decode('UTF-8')
        print(sonuc)
        
    except:
        print(hata_mesaji)
   
                      
                      
                      
def http():
    try:
        hedef = input("hedef adres url girin (http/https): ")
        #https://www.example.com
        url = ("https://api.hackertarget.com/httpheaders/?q=" + hedef)
        http = urlopen(url).read()
        sonuc = http.decode('UTF-8')
        print(sonuc)
        
    except:
        print(hata_mesaji)



def geo():
    hedef = input("ip adresi giriniz: ")
    # ip girin 74.55.242.34
    url = ("https://api.hackertarget.com/geoip/?q=" + hedef)
    geo = urlopen(url).read()
    sonuc = geo.decode('UTF-8')
    print(sonuc)
    


def zonetrans():
    hedef = input("hedef sorgu sitesi girin: ")
    url = ("https://api.hackertarget.com/zonetransfer/?q= " + hedef )
    zo = urlopen(url).read()
    sonuc = zo.decode('UTF-8')
    print(sonuc)
    
    
if islem == 1:
    reversedns()
elif islem == 2:
    search()
elif islem == 3:
    dns()
elif islem == 4:
    zone()
elif islem == 5:
    link()
elif islem == 6:
    http()
elif islem == 7:
    asm()
elif islem == 8:
    geo()
elif islem == 9:
    zonetrans()

