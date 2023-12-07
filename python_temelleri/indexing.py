import numpy as np 

numbers = np.array([0, 5, 10, 15, 20, 25, 50, 75])
result = numbers[5]   # 25
result = numbers[-1]  # 75
result = numbers[0:3]  # [0 5 10]
result = numbers[:3] # [0 5 10]
result = numbers[3:]  # [15 20 25 50 75]
result = numbers[::]  # [0 5 10 15 20 25 50 75]  # Baştan sona kadar tüm listeyi getir demek.
result = numbers[::-1]  # [75 50 25 20 15 10 0]  # Listeyi terse çevirdik.
result = numbers[::-2]  # [75 25 15  5]  # Sağdan sola doğru bir elemanı aldı bir elemanı almadı.


# Çok Boyutlu Bir Liste

numbers2 = np.array([[0,5,10],[15,20,25],[50,75,85]])
# print(numbers2)  # 3'e 3'lük bir matris olur.
result = numbers2[0]  #Burada satırları seçmiş oluyoruz.    #[50,75,85]
result = numbers2[2]
result = numbers2[0,2]  # 10   ilk satırı seçtik, 1.satırdaki 2.indeksteki elemanı (10) seçtik.

# Birden fazla satırdan belli elemanları seçmek istersek
result = numbers2[:,2]  # : ile tüm satırları seçmiş oluyoruz.Her satırdaki 2.indeksteki değerleri
#seçmiş olduk.  # Gelen değerler dizi içerisinde gelir.
result = numbers2[:,0]

result = numbers2[:, 0:2] 
result = numbers2[-1 , :]  # Son satırı seç ve tüm sütunları al.   [50,75,85]
# NOT: 0,15,50 1. kolon elemanları ,   5,20,75 2.kolon elemanlarıdır.
result = numbers2[:3,:3]
result = numbers2[:2,:2]
 # print(result)

# arr1 = np.arange(0,10)
# arr2 = arr1  #referans   # aynı adresi tutan yapılar
# arr2[0] = 20   # ikisinin de içeriği değişir.
# print(arr1)
# print(arr2)   # aynı şeyler yazılır.




arr1 = np.arange(0,10)
arr2 = arr1.copy()
arr2[0] = 20

print(arr1)
print(arr2)  # farklı yazılır,sadece arr2'nin içeriği değişir.