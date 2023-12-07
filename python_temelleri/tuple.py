list =[1,2,3]
# tuple da bir listedir. Parantezlerle tanımlanabilir veya parantez kullanmasan da olur.

tuple = (1, 'iki', 3)
# tuple = 1, 'iki', 3 şeklinde de olabilir.

print(type(list))
print(type(tuple))

print(list[2])
print(tuple[2])

print(len(list))
print(len(tuple))

# list = [ 'ali', 'veli'] # Listenin içerisine farklı elemanlar atayabiliriz.
# # Önceki içeriği sil ve tamamen farklı içerik ekle.
# tuple = ('damla', 'ayse', 'ayse') # Tuple'ın  içerisine farklı elemanlar atayabiliriz.
# # Önceki içeriği sil ve tamamen farklı içerik ekle.
# names = ('demet', 'emel', 'ayse') + tuple # Buradaki nesne üzerine tuple nesnesi üzerine eklendi.
# print(names)

# list[0] = 'ahmet' # Burada hata almayız.
# # tuple[0] = 'eda' # Burada hata alırız : Tuple da herhangi bir elemana atama yapamayız.
# # # Tamamen yeni liste yapabilirsin ama tek  bir eleman üzerinde değişiklik yapamazsın !
# print(list)  # ['ahmet ', 'veli' ]
# # print(tuple) # Hata

# print(tuple.count('ayse'))

# print(tuple.index('ayse'))  # ayse tuple nesnesi üzerinde ilk nerede var oluyor bulur. 1 numaralı indexte bulur.
