# Dictionary : Kullanılabilecek bir liste tipi
 
# key - value

# 41 => Kocaeli  34 => İstanbul

# sehirler = ['Kocaeli', 'İstanbul']
# plakalar = [41, 34]

# print(plakalar[sehirler.index('Kocaeli')])  # Bu  bildiğimiz haliydi. ==> 41

# Bizim istediğimiz 
# print (plakalar['Kocaeli']) => 41 olması
# print (plakalar['İstanbul']) => 34 olması

# Amaç tek liste üzerinden key ve value bilgisine erişmek 

#                         plakalar = { 'key': 'value'}

plakalar = { 'Kocaeli' : 41 , 'İstanbul' : 34 } 

print(plakalar['Kocaeli'])
print(plakalar['İstanbul']) # Key'i yazdığında sana sonucu verecek.Key'i köşeli parantez ile iste.

# Plakalar içinde olmayanı plakalar içerisine eklersek 

plakalar ['Ankara'] = 6  # Bu şekilde yaparak 'Ankara' : 6 bilgisini de plakalar içerisine eklemiş olduk.
print(plakalar)  

plakalar['Kocaeli'] = 'new value'  # Burada Kocaeli' ye yeni value atadık.
print(plakalar)
# Yani Dictionary elemanlarına ulaşıp onlar üzerinde güncelleme yapabilirsin.

# users = {
#     'sadikturan' : 36 ,
#     'cinarturan' : 2
# }
# print(users['cinarturan'])    # ==> 2

# Sadece bir value bilgisi değil içinde daha fazla bilgi olsun isterse

users = { 
    'sadikturan' : {
        'age' : 36 ,
        'roles' : ['user'] ,
        'email' : 'sadik@gmail.com',
        'address' : 'Kocaeli',
        'phone' : '123123123'
    },
    'cinarturan' : {
        'age' : 2 ,
        'roles' : ['admin','user'] ,
        'email' : 'cinar@gmail.com',
        'address' : 'Kocaeli',
        'phone' : '456456456'
    }
}
print(users['cinarturan'])

print(users['cinarturan']['age'])
print(users['cinarturan']['email'])
print(users['cinarturan']['address'])

print(users['cinarturan']['roles'])  # ['admin','user']
print(users['cinarturan']['roles'][0]) #admin

