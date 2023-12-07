class Person : 
    # pass # yer tutucu olarak kullanılır.Methods veya attributes olmazsa hata almamak için kullanılabilir.

    #class attributes
    address = 'no information'

    #object attributes : (object seviyesinde attributes tanımlama)
    # constructor (yapıcı metod) içerisinde tanımlanırlar.
    # self parametresi : Classtan türetmiş olduğumuz p1 veya p2 objesi.
        # obje üzerine bir değer aktarmak istersen self'i kullanacaksın.
        # self'in üzerine hangi attributes(özellikleri) eklemek istiyorsan selfden sonraki paramatre olarak 
        # belirteceksin bunlara da kullanıcının göndermiş olduğu name ve year'ı aktaracaksın.
    def __init__(self, name, year):
        # object attributes 
        self.name = name
        self.birthyear = year  #birthyear yerine year da diyebilirsin.
        # Kullanıcının göndermiş olduğu year bilgisini birthyear'a atadık.
             # Önemli olan p1 objesi üzerinden name ve year alanına ulaşabiliyor olmak.
        print(' init metodu çalıştı.')
   

        # !!! init metodu oluşturulan her bir obje için mutlaka çalışır.
        # Yani biz obje üzerinden init metodunu çağırmayacağız.
        # Person classından p1 objesi oluşturulduğunda init metodu çalışır.

    # methods
    
     


# class' ı yazdıktan sonra methods veya attributes belirtmen gerekir, yoksa hata alırsın.

# if a>10 :
#pass
# Burada normalde bir şey yazman gerekir, yazmazsan pass kullanabilirsin.


# object (instance) tanımlama
# Küçük harfle tanımlanırlar ve sayısal bir ifade ile tanımlanmıyorlar.

# p1 = Person() #  p1 objesini tanımlamış olduk.
# p2 = Person() #  p2 objesini tanımlamış olduk.
# p1 objesi üzerinden Person classındaki methods ve attributes'e ulaşabiliriz.
# print(p1)
# print(p2)
#Yukarıdaki gibi yazdırırsan
# p1 ve p2 :Farklı adreslerde tanımlanmış 2 tane obje ve bu objelerin tipi Person'dır.
# print(type(p1))  # Objenin tipini (type) yazdırdığında Person tipinde olduğunu görürüz
# print(type(p2))  # Objenin tipini (type) yazdırdığında Person tipinde olduğunu görürüz
# print(p1 == p2)  #False olduğunu görürüz. Farklı objeler olduğunu görürüz.


# p1 = Person() #    p1 objesini tanımlamış olduk. (Bu şekilde çalıştırırsan hata alırsın.)
# sen obje türettin ama parametre yollamayı unuttun .
# self için parametre yollamana gerek yok. self yerine örneğin this de koyabilirsin fark etmez.
# önemli olan ilk parametrede yer alıp görevini yerine getirmesi.
# self oluşturulacak olan objeleri temsil ediyor.
p1 = Person('Sıla', 2003) # Yapman gereken 
p2 = Person('Esra',2011) # Yapman gereken 
     # Çıktıda iki tane init metodu çalıştı yazısı olacak.
    
     # Şu şekilde de yapabilirsin :
# p1 = Person(name ='Sıla',year =2003)
# p2 = Person(name ='Esra',year =2011)

# updating 
p1.name = 'Beyza'  # Sıla ismi yerine Beyza ismi yazılır. (p1 için)
p1.address = 'Kocaeli' # Adres bilgisi Kocaeli olarak değişir. (p1 için)

# Objeler üzerinden bütün attributeslere ulaşabiliriz.
# (Bu attributeslerin class veya constructor içerisinde tanımlanmış olması önemli değil.)


# Gönderdiğimiz p1 ve p2 objelerinin değerlerini ekrana yazdırırsak 
# Burada yaptığımız işlem : accessing object attributes 
print(f' p1 : name:{p1.name}, year:{p1.birthyear}, address:{p1.address}')
print(f' p2 : name:{p2.name} ,year:{p2.birthyear}, address:{p2.address}') 











