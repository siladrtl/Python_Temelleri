# print(5000-(5000*.27))
# print(4000-(4000*.27)) bunlar yerine değişkenlere değer atayabiliriz.
maasAli=5000
maasAhmet=4000
vergi=0.27
print( maasAhmet -( maasAhmet * vergi))
print( maasAli-(maasAli * vergi ))
#       #:yorum satırı demek 
#Değişken Tanımlama Kuralları
# 1)Rakam ile başlayamaz, _ ile başlayabilir .   1number olamaz , number1 olabilir, _number olabilir.
# 2)Değişkene değer atamak zorundasın. number1=10 gibi , sadece number1 olarak bırakamazsın.
# 3) Aynı değişken ismini aynı program içerisinde birden fazla kullanamazsın.
# number1=10 number1=20 yaptığında farklı bir değişken tanımlamış olmazsın.

number1=10
print(number1)

number1=20
print(number1)

number1+=30
print(number1)

# 4) Büyük küçük harf duyarlılığı vardır.Türkçe karakter kullanılmaz.
age=20
AGE=30
print(age)
print(AGE)

x=1      #int 
y=2.3    #float
name="Çinar"    #string
isdStudent=True #bool 

#x,y,name,isStudent = ( 1, 2.3, 'Çinar' , True)  #Hepsini tek satırda değer atayabilirsin.

# a=10
# b=20
# print(a+b) sonuç 30 olur


a='10'
b='20'
print(a+b)  # sonuç 1020 olur.

firstName= 'Sila'
lastName= ' Dertli' 
print(firstName+lastName)  #Sıla Dertli
# 5) Tanımladığın değişkenler arasında boşluk olamaz.  last Name olamaz , last_Name oalbilir.


