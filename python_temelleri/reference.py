# Bir veri tipinde obje , değişken tanımlandığı zaman bilgisayar (bellek) üzerinde nasıl değerlendiriliyor?

# Value Types ==> number(float,int) , string 
# x = 5
# y = 25

# x = y  # y değerini x'e aktardık.

# y = 10 
# print( x, y) # 25 10   # y'nin üzerinde yaptığımız bir değişiklik x'i etkilemez.

# Reference Types ==> list , class

a = ['apple', 'banana']
b = ['apple', 'banana']

a = b
b[0] = 'grape'  # b üzerinde yapılan bir değişiklik a'yı da etkiledi 
# çıktı  ['grape' , 'banana'] ['grape' , 'banana'] olur.
# a ve b aynı değeri gösteriyor.
print(a,b)  

# Özetle value typler ile ilgilenirken verinin kendisiyle, reference typler da ise listenin kendisiyle 
# ilgileniyoruz