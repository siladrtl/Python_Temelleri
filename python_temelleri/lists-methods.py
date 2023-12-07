numbers = [1, 10, 5, 16, 4, 9, 10]
letters = ['a', 'g', 's', 'b', 'y', 'a', 's']

val = min(numbers)
print(val) #1

val1 = max(numbers)
print(val1) #16
 
vals2 = max(letters)
print(vals2)   # y 

# Liste elemanlarını parçalamak istersek 
val3 = numbers[3:6] # 3 dahil 3. indeksten 6.indekse kadar olan değerleri al.(6.indeks dahil değil)
print(val3)  
val4 = numbers[ :3] # Baştan başla 3.indekse kadar olan değerleri al, 3.indeks dahil değil.
print(val4)
val5 = numbers[4:] # 4.indeksten başla sona kadar git.(Son da dahil.)
print(val5)

numbers[4]= 40 
print(numbers)  # 5.eleman artık 40 olur.

# #Liste üzerine bir eleman eklemek istediğin zaman
# numbers.append('49') # En sona 49'u string olarak ekledik.
# # Sayı olarak eklemek istersen ' ' kullanmana gerek yok.
# print(numbers)

# # İstediğin bir konuma eklemek istersen 
# numbers.insert(3 , 78) # 3.indeksten hemen önce 78 sayısını ekle.
# # numbers.insert(-1,52)  # en sondaki indeks numarasından bir önce 52 numarasını ekler.
# #Buralarda verdiğimiz indeks numarasından önce sayılar eklenir.
# print(numbers)

# Elemanları silmek için 
# numbers.pop() # Sondaki '49' elemanını sildi.
# print(numbers) 
# numbers.pop(0)  # 0.indeks elemanını siler, yani 1'i siler.
# print(numbers)
# numbers.pop(-1) # En sondaki elemanı siler. '49' elemanını sildi.
# print(numbers) 

# numbers.remove(16) # Silmek istediğin elemanı yazarsın , 16 silinir.
# print(numbers)

# Sıralama İşlemleri
numbers.sort() # Rakamları küçükten büyüğe sıralar.
numbers.reverse() # Listeyi sıraladıktan sonra tam tersine çevirdi.Büyükten küçüğe de sıraladı.
print(numbers)

letters.sort()  # Harfleri alfabetik olarak sıralar. 
letters.reverse() #Harf sıralamasını tam tersine çevirir. z'den a'ya şeklinde olur.
print(letters)

# print(len(numbers)) : numbers 'ın eleman sayısını verir.
 # numbers üzerinden count metodunu çağırarak istediğimiz bir elemanın kaç tane olduğunu görebiliriz.
print(numbers.count(10)) # numbers da 2 tane 10 var.
print(letters.count('a')) # letters da 2 tane a harfi var.

numbers.clear()
print(numbers) #Elemanlar temizlenir ve boş bir dizi karşımıza çıkar.
# Bütün elemanları silmek için clear metodunu kullanabiliriz.