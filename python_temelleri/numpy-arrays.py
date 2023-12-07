import numpy as np
# result = np.array([1,3,5,7,9])  #Köşeli parantez içerisinde tek bir parametre yolladığımızdan emin oluyoruz.
# result = np.arange(1,10)  # 1 dahil 10 dahil değil.
# result = np.arange(10,100,3) # üçer üçer artacak , 100 dahil değil.
# result = np.zeros(10) # 10 tane sıfırdan oluşan köşeli parantez
# result = np.ones(10)  # Her eleman float bir değere karşılık geliyor.
# result = np.linspace(0,100,5) #Verilen başlangıç ve bitiş değerini eşit aralıklarla böler.  
# [   0.  25.  50.  75. 100.]
# result = np.linspace(0,5,5)    # [0.   1.25 2.5  3.75 5.  ]
result = np.random.randint(0,10) # 0 dahil 10 dahil değil , her zaman farklı bir int değeri çıkar
# result = np.random.randint(20) # Sadece üst değeri de verebilirsin. 0 dahil 20 yok
# result = np.random.randint(1,10,3) # 1 ile 10 arasında 3 tane değerin olduğu bir dizi oluşturur.
# result = np.random.rand(5) # 0 ile 1 arasında 5 tane sayıdan oluşan bir dizi 
# result = np.random.randn(5) # 0 ile 1 arasında 5 tane sayıdan oluşan bir dizi , - değerler de işin içine girer.
# result = np.arange(50) # 0'dan 50'ye kadar bir dizi olur,50 dahil değil.

# np_array = np.arange(50)
# np_multi = np_array.reshape(5,10)  # 5 satır 10 sütundan oluşan matris oluşur.
# print(np_multi.sum(axis=1))  # Oluşturduğumuz matrisin satırlarının toplamını veren bir dizi oluşur
# print(np_multi.sum(axis=0))  # Oluşturduğumuz matrisin sütunlarının toplamını veren bir dizi oluşur

# rnd_numbers = np.random.randint(1,100,10)  # 1 ile 100 arasında 10 tane sayı üretilir.
# print(rnd_numbers)
# result = rnd_numbers.max() 
# # result = rnd_numbers.min()
# # result = rnd_numbers.mean() # Sayıların ortalamasını alır.
# # result = rnd_numbers.argmax()  # Üretilen sayılardan en büyük olanının indeks numarasını yazar. 
# # result = rnd_numbers.argmin()  # Üretilen sayılardan en küçük  olanının indeks numarasını yazar.               
print(result)  # Sayılar arasında en büyük olan sayıyıyı yazar.

