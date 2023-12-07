website = "http://sadikturan.com"
course = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"


# 1) ' Hello World ' karakter dizisinin baş ve sonundaki boşluk karakterlerini silin.
result = ' Hello World '.strip()
# result = ' Hello World '.lstrip() # Sadece soldaki boşluğu silmek istersen.
# result = ' Hello World '.rstrip() #Sadece sağdaki boşluğu silmek istersen.

# website da sadece sadikturan.com ifadesi kalsın istiyorsan soldan silme işlemi yap.
result1 =website.lstrip('/:pth')  #Her karakter bir kere yazılır

# 2) 'www.sadikturan.com' içindeki sadikturan bilgisi haricindeki her karakteri silin.

#sağdan ve soldan silme işlemi yaptığımız için direkt strip yazarız.
result2 = 'www.sadikturan.com.'.strip('w.com')

# 3) 'course' karakter dizisinin tüm karakterlerini küçük harf yapın.
result3 = course.lower()
# 4) 'website' içinde kaç tane a karakteri vardır? (count('a'))
result4 = website.count('a')
# result4 = website.count('www') #ifadesinden kaç tane vardır görebilirsin ya da 
# result4 = website.count('www',0,10) #0.indeksten başlayıp 10.indekse kadar kaç tane var görebilirsin.

# 5) 'website' www ile başlayıp com ile bitiyor mu ?
result5 = website.startswith('www')
result6 = website.endswith('www')
# 6) 'website' içinde '.com' ifadesi var mı ?
result7 = website.find('.com')  # çıktı ,17.indeksten itibaren .com ifadesi vardır anlamına gelir
# result7 = website.find('.com',0,10) # 0 ile 10.index arasında bu değer var mı kontrol eder.
# 7) 'course ' içindeki karakterlerden hepsi alfabetik mi ? (isalpha, isdigit)
# 8) 'Contents' ifadesini satırda 50 karakter içine yerleştirip sağ ve soluna * ekleyiniz.
# 9) 'course' karakter dizisindeki tüm boşluk karakterlerini '-' ile değiştirin.


print(result)
print(result1)
print(result2)
print(result3)
print(result4)
print(result5)
print(result6)
print(result7)