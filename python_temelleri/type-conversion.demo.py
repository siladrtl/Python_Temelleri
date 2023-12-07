'''
Dairenin alanini ve cevresini bulunuz
alan:πr*2
çevre:2πr
'''
pi=3.14
r=float(input('Dairenin yaricap:')) 
#Yarıçapı float da girebilir.
#Yarıçap  olarak 2a girersen eğer ValueError hatası verir.
#inputtan bir değer okuduğun zaman sana string değerinde verir.
# r=float(r) Şeklinde de tür dönüşümü yapabilirsin.
alan=pi*(r**2)
print('Dairenin alanı :' , alan)
cevre=2*pi*r
print('Dairenin cevresi:',cevre)

#string birleştirme : print('alan : ' + alan + 'cevre : ' + cevre ) 
#Burada hata alırız float değerleri str olarak birleştiremezsin.

#string birleştirme : print('alan : ' + str (alan) + 'cevre : ' + str (cevre) ) 
#Tür dönüşümünü yaparak hatadan kurtulursun.