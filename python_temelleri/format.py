name = 'Sıla'
surname='Dertli'
print('My name is {}'.format (name)) #Formata yolladığın süslü parantez yerine geçer.
print('My name is {} {}' .format(name , surname)) 
#yorum satırını kaldırmak için ctrl k + ctrl u yapılır.
print('My name is {0} {1}' .format(name , surname)) #Sıla Dertli
print('My name is {1} {0}' .format(name , surname)) #Dertli Sıla
print('My name is {s} {n}' .format(n=name , s=surname)) #Dertli Sıla

print("My name is {} {} and I'm {} years old." .format(name , surname,'20'))
# Başlangıca age=20 bilgisini tanımlayıp .format(name,surname,age) yazarak da üsttekine ulaşırsın.
#Burada age için number bilgisini tür dönüşümü yapmadığımıza dikkat edelim.

print("My name is {} {} and I'm {} years old." .format(name , name , name)) #Her yerde Sıla yazıyor.


result=200/700
print('The result is : {}' . format(result)) #Çıktıdaki uzun sonucu formatlamak istersek alttaki işlemi yaparız.
#Normalde sonuç 0.285714.. ama biz aşağıdaki sayesinde
print('The result is : {r:10.3}' . format(r=result)) #0.286 olur.
#Burada 3 virgülden sonra kaç basamak olacağını temsil ediyor.
#10 ise tam kısım için kaç karakterlik bir boşluk bırakacağını gösterir.
# (The result is: in yanından bırakacağı boşluk miktarı)
#Saymaya sayının kendisi de dahil sağdan sola doğru sayar sonra boşluk bırakır.


#f string

print(f"My name is {name} {surname}.") #Tırnağın başına f ekledik. 