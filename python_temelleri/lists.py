# message = 'Hello There. My name is Sadık Turan'.split()
#.split() ile diziye (listeye) çeviriyoruz.
# print(message) # Her bir kelimeyi tek tek bir dizinin elemanıymış gibi yazar.(Dizi köşeli ayracı kullanılarak)
# print(message[0]) #Dizinin ilk elemanı olan Hello çağırılmış olur.

# message = 'Hello There. My name is Sadık Turan'
# print(message[0]) #.split() metodunu çalıştırmadığında dizi üzerinden çağırdığında string ifadenin ilk elemanı
# olan H gelir.

# my_list = [1,2,3]
# my_list= ['bir', 2 ,True ,5.6] #Liste elemanlarının hepsinin tipi birbirinden farklı.
# print(my_list)

list1 = ['one','two','three']
list2 = ['four','five','six']
numbers = list1 + list2
print(numbers)
print(len(numbers))
print(numbers[2])

userA = ['Sadık', 36]
userB = ['Çınar', 2]
users = userA + userB
print(userA)
print(userB)
print(users)

#liste içerisinde liste olsun istiyorsan (dizi içerisinde dizi olsun)

users = [userA , userB]
print(users) # Dizinin içerisinde iki tane dizi var.
print(users[1])
# Çınar ismine ulaşmak istiyorsan 
# a = users[1]
# print(a [0])
print(users[1][0])