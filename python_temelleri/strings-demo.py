website ='http://www.sadikturan.com'
course ='Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 Saat)'

# 1) 'course' karakter dizisinde kaç karakter bulunmaktadır?
result = len(course)
print(result)

# 2) 'website' içinden www karakterlerini alın
result2 = website[7:10]
print(result2)
# 3) 'website' içinde com karakterlerini alın
#sayarak : result3=wwebsite[22:25] , print(result3) ya da
length=len(website)
result4 = website[length -3 : length]
print(result4)

# 4) 'course' içinden ilk 15 ve son 15 karakterlerini alın 
result5 = course[ :15]  # Bunu course[0 :15] ile de yapabilirsin.
print(result5)

#   course[-15 : -1] yaparsan Çıktı işleminde kapama parantezini almıyor.
#Bu işlemde ilk başta başlangıç indeksinin verilmesi lazım, bu yüzden -1 den başlayamaz
# -15'den başlar.
#e den başlıyor ama e yi yazmıyor.

result6 = course[-15 : ]
print(result6)


# 5) 'course' ifadesindeki karakterleri tersten yazdırın

#Course ifadesindeki tüm elemanları almak için course [::] kullanmak gerekir.
# Böylelikle course'ın tamamını yazmış olursun.
# : ' yı sola course[ : 15] koyarsan sol tarafı tamamen işin içine katmış olursun.
# sağ tarafa course[15 : ] koyarsan ise bitiş karakterlerini işin içine katmış olursun.
# course[::1 ] yaparsan course ın tamamını ekrana yazdırırsın.
# course[::2] yaparsan adım sayısını belirtmiş olursun, burada her karakteri almaz.
# 2 karakter de bir yazılır.

result7 = course[ :: -1 ] #tüm karakterleri al ve sağdan sola doğru yaz.
print(result7)
s='12345' * 5
print(s[::5]) #O'dan başlayarak elemanları sayarsak 5.eleman 1'e denk gelir ve 5 kere 1 yazılmış olur.

name , surname, age , job = 'Bora' , 'Yilmaz', 32 ,'Mühendis'

# 6) Yukarıdaki verilen değişkenler ile ekrana aşağıdaki ifadeyi yazdırın
#     'Benim adım Bora Yılmaz , Yaşım 32 ve mesleğim Mühendis.'
result9 ='Benim adım ' +name+ ' ' +surname+ ' ' +',Yaşım'+ ' ' +str(age)+ ' '  've mesleğim '+job
print(result9)
#ya da daha kolay şekilde de yapabilirsin 
result10 = 'Benim adım {} {} ,Yaşım {} ve mesleğim {}.'.format(name,surname,age,job)
print(result10)
#Burada tür dönüşümü yapmana gerek yok.
#.format(name,surname,age,job) sırası önemlidir!
#Değişkenlerin içeriklerinin sırasını değiştirmek istiyorsan index numarası verebilirsin.
#'Benim adım {0} {1} ,Yaşım {2} ve mesleğim {3}.'.format(name,surname,age,job)
#Bunu çalıştırırsak yine aynı sonuca varır.

result11= 'Benim adım {1} {0} ,Yaşım {3} ve mesleğim {2}.'.format(name,surname,age,job)
print(result11)
#Burada ise yer değişikliği olur.

result12 = f'Benim adım {name} {surname} ,Yaşım {age} ve mesleğim {job}.'.format(name,surname,age,job)
print(result12)
# En kolay şekilde tırnağın dışında f kullanarak yapabilirsin.

# 7) Hello world ifadesindeki w harfini 'W' ile değiştirin

s1='Hello world' # w 6.index numarasına denk gelir.
s1= s1[0:6] + "W" + s1[-4 : ]
print(s1)
# Bunun kolay yolu ise 
# s1.replace('w','W')


 # 8) 'abc' ifadesini yan yana üç defa yazdırın. 
result14 = 'abc'*3
print(result14)

#result14 = 'abc '*3    #araya boşluk eklemek için kullanabilirsin.