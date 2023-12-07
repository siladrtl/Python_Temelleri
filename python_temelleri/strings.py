name = 'Sila'
surname = 'Dertli'
age=20
# print ('My name is : '+ name + ' ' + surname + 'and I am '+ age +  'years old.') 
#Burada hata alacaksın string ifadeleri toplamaya çalışıyorsun ama age string değil.
#ya age ='20' yap ya da print içerisinde str(age) yapıp tür dönüşümü yapmış ol.
# Ayrıca     deneme='My name is '      yapıp 
#print(deneme + name +' ' + surname) şeklinde oluşturabilirsin.

print ('My name is : '+ name + ' ' + surname + ' ' +'and \nI am '+ str(age) + ' '  +'years old.')
# \n : Bu işareti koyduğun yerden itibaren alt satıra geçmeni sağlar.
# \nI yazılırsa iki cümle alt satırda aynı hizaya denk gelir,arada boşluk bırakırsan sağdaki 
# hizaya kayar
greeting='My name is : '+ name + ' ' + surname + ' ' +'and \nI am '+ str(age) + ' '  +'years old.'
#yapıp print(greeting) yaparsan yine aynı şekilde bilgi karşına gelir.
#Sıla kelimesi string (karakter) dizisinin bir elemanı
#soldan başlarsan 0 dan artacak, sağdan başlarsan -1 den azalacak şekilde index numaraları vardır.

print(greeting[0]) #greeting dizisinin 0.index numarasına sahip  olan M ekrana yazılır.
print(greeting[2]) #boşluk karakteri gelir. 0-1-2 yaparsak sırada boşluk oluyor.

print(len(greeting)) #greeting dizisinin kaç karakterden oluştuğunu bize söyler.

print( greeting [ len ( greeting ) -1] ) #Son karakteri görmemizi sağlar.
 # ya da 
length = len(greeting) 
print(greeting[length-1]) # son karakteri görebilirsin
print(greeting[-1]) # son karakteri elde edebilirsin

print(greeting[3:7]) # 3.karakter dahil değil 4 5 6 7. karakterleri yazmayı sağlar.
print(greeting[3:]) # 3.karakter dahil değil,sonuna kadar yazar.
print(greeting[ :48]) # Hepsini yazdı.
print(greeting[ :15]) #Başlangıçtan itibaren al , son karakter 15.olsun
print(greeting[2:40:2]) #2 den 40 a kadar git, her karakteri alma , 2 karakterde 1 al.1 ini al ,1 ini alma.

