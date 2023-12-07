# Set tanımlamak için tanımlamayı süslü parantezler içerisine yaparız.

fruits = {'orange', 'apple', 'banana'}
# print(fruits)

# Set' e index bilgileri ile ulaşamazsın,indexlenemez !
# print(fruits[0]) ==> HATA 
# Çıktıda her seferinde farklı bir sıralama ile çıkıyor.
# Listeyi sıralayamazsın.

# Elemanlara döngü kullanarak ulaşabilirsin
# for x in fruits: 
#     print(x)

    # Listeye nasıl bir eleman eklenir ?
fruits.add('cherry')   #.add metodu ile ekleyebilirsin
# Birden fazla eleman nasıl ekleyebilirsin ?
# add'i art arda kullanarak veya update ile liste gönderebilirsin.
fruits.update(['mango','grape','apple'])
fruits.remove('mango')  # mango bilgisi listeden silinir.
fruits.discard('apple') # apple bilgisi listeden silinir.
print(fruits)

# fruits.pop() : fruits üzerinden pop metodunu çalıştırdığımızda indexlenen bir liste olduğunda 
# son eleman silinebiliyordu.
# Ancak fruits için bu gerçekleşmeyebilir..Çünkü elemanlar sıralanmamış ve sadece son elemanın silineceğini 
# garanti altına alamayız.
# Herhangi bir eleman da silinebilir.
fruits.clear()  # Tüm elemanlar silinir.
print(fruits)  # Çıktıda set() yazısı çıkar.

myList = [1,2,5,4,4,2,1]
print(myList) # Elemanların tamamı listede gözükür.

print(set(myList))  #Tekrarlayan elemanlar liste içerisinden çıkarılır.
# # 4'ü çıktıda 1 kere görürüz.Elemanlar tekrarlanamaz.

# Aynı elemanı bir daha yollarsan çıktıda iki kere görmezsin.
# Elemanlar liste içerisinde tekrarlanamaz.
