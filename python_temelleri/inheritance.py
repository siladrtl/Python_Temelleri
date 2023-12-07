# class Person () : 
#     def __init__(self) :
#         print('Person Created')
# class Student (Person) :  # Student, Person'dan miras alıyor.
#     pass         
# p1 = Person()   # çıktı Person Created
# s1 = Student()  # çıktı Person Created

# class Person () : 
#     def __init__(self) :
#         print('Person Created')
# class Student (Person) :  # Student, Person'dan miras alıyor.
#     def __init__(self) : 
#         Person.__init__ (self)   # Person Created 
#         print('Student Created')

# p1 = Person()
# s1 = Student()  


class Person () :
    def __init__(self, fname, lname) :
        self.firstName = fname
        self.lastName = lname
        print('Person Created ')
        
    def who_am_i (self) :
       print('I am a person.')

    def eat(self) : 
       print('I am a eating')   

class Teacher (Person) :
   def __init__(self,fname,lname,branch)  :
      super().__init__(fname,lname)    # self'i göndermene gerek yok. 
      self.branch = branch
   def who_am_i(self):
       print(f'I am a {self.branch} teacher')

class Student(Person) :
 def __init__(self,fname,lname,number ):
    Person.__init__(self,fname,lname)
    self.studentNumber = number
    print('Student Created')
    
    #override 
    # Aynı isimdeki metod temel sınıftaki metodu ezer.
 def who_am_i(self) :   # Student üzerinden I am a person ' ı ezmek için kullanabilirsin.
   print('I am a student')  

 def sayHello(self) :
    print('Hello. I am a student')

p1 = Person('Sıla','Dertli')
s1 = Student('Esra','Dertli',35)
t1 = Teacher('Beyza','Dertli','Math')

print(p1.firstName + ' ' + p1.lastName)
print(s1.firstName + ' ' + s1.lastName + ' ' + str(s1.studentNumber))

p1.who_am_i()
s1.who_am_i()
t1.who_am_i()

p1.eat()
s1.eat()

s1.sayHello()






