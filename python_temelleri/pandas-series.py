import pandas as pd
import numpy as np


# data 
numbers = [20, 30, 40, 50]
# numbers = np.array([20, 30, 40, 50])  # np.array kullanılarak yapılabilecek tanımlama
letters = ['a', 'b', 'c', 20]  # Pandas da farklı tipte veri koyabilirsin ama numpy de  koyamazsın
scalar = 5
dict = {'a':20 , 'b':30 ,'c':30 , 'd':40}
random_numbers = np.random.randint(10,100,6)  # 10 ile 100 arasında(100 dahil değil) 6 tane int değer 

# pandas_series = pd.Series()
# print(pandas_series)   #  Series([], dtype: object)

# pandas_series = pd.Series(numbers)
# pandas_series = pd.Series(letters)   # içeride str değer varsa dtype : object 
# pandas_series = pd.Series(scalar)
# pandas_series = pd.Series(5 , [0,1,2,3])
# pandas_series = pd.Series(numbers , ['a', 'b', 'c', 'd'])  # Burada a b c d 'yi numbers'a indeks olarak atadık.
# pandas_series= pd.Series(dict)
# pandas_series = pd.Series(random_numbers)
pandas_series = pd.Series([20, 30, 40, 50] , ['a', 'b', 'c', 'd'])

result = pandas_series[0]   # 20 # (indeks yazmıyor)
result = pandas_series[-1]  # 50   # Sağdan ilk elemanı (indeks yazmıyor)
result = pandas_series [:2]  # 0 ve 1. eleman  (indeks değerleri ile birlikte yazar)
result = pandas_series [-2:]  # Sağdan ilk ve ikinci eleman (indeks değerleri ile birlikte yazar)
result = pandas_series['a']   # 20
result = pandas_series['d']   # 50
# result = pandas_series [['a','c','e']]    # KeyError: ['e'] not in index
result = pandas_series.ndim  # 1 boyutlu bir dizi 
result = pandas_series.dtype
result = pandas_series.shape  
result = pandas_series.min()  # 20
result = pandas_series.max()  # 50
result = pandas_series.sum()  # 140  (20+30+40+50)
result = pandas_series + pandas_series
result = pandas_series + 50
result = np.sqrt(pandas_series)

result = pandas_series >= 50
result = pandas_series % 2 == 0
# print(pandas_series[pandas_series % 2 == 0])


# print(pandas_series)
# print(result)

opel2018 = pd.Series([20, 30, 40, 10 ],['astra', 'corsa', 'mokka', 'insignia'])

opel2019 = pd.Series([40, 30, 20, 10 ],['astra', 'corsa', 'Grandland', 'insignia'])

total = opel2018 + opel2019
print(total)      # Grandland     NaN
                  # astra        60.0
                  # corsa        60.0
                  # insignia     20.0
                  # mokka         NaN  # Hata vermedi NaN yazdı.
                  # dtype: float64
print(total['astra'])
# print(total['combo']) 