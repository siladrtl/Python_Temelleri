# # class attributes'in , init'in ve methods'ın aynı hizada olması gerekir.
# class Person : 
   
#  #class attributes
#  address = 'no information'
 
#  # constructor (yapıcı metot)
#  def __init__(self, name, year):
#         #object attributes 
#         self.name = name
#         self.birthyear = year
        
# # instance methods  ==> Oluşturduğumuz objelere hizmet edecek olan metot
#  def intro (self):   # self ile , tanımlanan objenin bir referansını verdik.
#    print('Hello There. I am ' + self.name)   #sağa kaydırman gerekiyor dikkat et.
# # instance methods 
#  def calculagateAge(self):
#      return 2019 - self.birthyear
    
# # object (instance) 
# p1 = Person(name ='Sıla',year =2003)
# p2 = Person(name ='Esra',year =2011)

# p1.intro()  
# p2.intro()
# print(f'adım : {p1.name} ve yaşım : {p1.calculagateAge()}')
# print(f'adım : {p2.name} ve yaşım : {p2.calculagateAge()}')
# # Metot çağırırken ve obje oluştururken class ile aynı hizaya denk gelecek şekilde yazıp çağırmalısın.
# # self address'e , name'e ve year'e ulaşabilir.


class Circle : 
    # Class object attribute
    pi = 3.14  # Ayrıca pi objesinin pi attributes'ini class seviyesinde tanımlamamış olmamız her bir
    # tanımlanan obje için ortak bir değer olması ve burada tanımlamazsak tek tek constructor'a eklememiz gerekirdi.
    

    def __init__(self, yaricap=1) : 
        self.yaricap = yaricap  # self.yaricap'ta yaricap yerine farklı bir şey yazabilirsin.
        # dışarıdan yaricap bilgisi geliyor.

        # Methods
    def cevre_hesapla(self) :  # Class'ın içerisindeki bilgilere ulaşmak için self parametresi alacak.
        return 2 * self.pi * self.yaricap
    
    def alan_hesapla(self) :
        return self.pi * (self.yaricap ** 2)
    
c1 = Circle() # yaricap = 1 olur class ile aynı hizada objeyi tanımla
c2 = Circle(5) # yaricap'a 5 atılır.

# Tanımlamış olduğumuz objelerin self parametresiyle ulaşılabilir olması pi değerine ve yarıçap bilgisine 
# ulaşmayı sağlar.
print(f'c1 : alan = {c1.alan_hesapla()} cevre : {c1.cevre_hesapla()}')
print(f'c2 : alan = {c2.alan_hesapla()} cevre : {c2.cevre_hesapla()}')


        

        
    
