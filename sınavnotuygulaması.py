def not_oku():
    dosya = open('sınav_notlar.txt','r')
    okunan = dosya.readlines()
    print(okunan)
    dosya.close()
def not_gir():
    ders = input('Ders Adı: ')
    vize = int(input('Vize: '))
    final = int(input('Final: '))
    ort = vize*4/10 + final*6/10

    
    dosya = open('sınav_notlar.txt','a')
    yazılacak = (ders +' dersi ' + ' vizesi: '+ str(vize)  + ' finali: ' +  str(final) + ' ortalama: '+ str(ort)+ '--------------'+'\n')
    dosya.write(yazılacak)
    dosya.close()
                


while True:
    print('Sayın Eşref Altuğ\nHoşgeldiniz... ')
    islem = int(input('1-Notları Oku\n2-Notları Gir\n3-Çıkış\n'))

    if islem == 1:
        not_oku()
    
    elif islem == 2:
        not_gir()
       

    else:
        break
    
   
    
    
    









    
