message = 'Hello There. My name is Sıla Dertli.'

# message = message.split()
# string bilginin her bir tanesi boşluk karakterlerinden itibaren bölünür ve bize karakter dizisi olarak verir.
# print(message[0])    # 0. index elemanı olan Hello yazdırılır.

# message = ' '.join(message)
# Boşluğun içinde de boşluk var dikkat et.
# message = '*'.join(message)   # Kelimelerin arasında * olur
# print(message)
 
#ayrılan ifadeleri birleştirmek istersen 
# message = ''.join(message)
# Parça parça olan elemanları birleştirecek ve araya da boşluk ekleyecek,eski haline çevirecek.


# message = message.split('.')
#String ifadeyi noktalardan itibaren ayırır ve bize karakter dizisi olarak verir.

# message = message.strip ()
# Kontrolü sağlar.Baştaki boşluk karakteri gider.

# message = message.upper() 
# message üzerinden upper metodunu çalıştırdığımızda mesaj değişkeni içerisindeki 
# tüm karakterler büyük hale gelir ve sonucu ise tekrar mesaj değişkeni içerisine aktarır.

# message = message.lower() yaparsan tüm karakterler küçük hale gelir.
# message = message.title() yaparsan her kelimenin baş harfi büyük hale gelir.
# message = message.capitalize() verilen string ifadenin sadece ilk kelimesinin baş harfi büyük olur.

# Verilen cümle içinde Sıla bilgisi var mı yok mu aramak istersen

index = message.find('Sıla')
print(index)
# Çıktıda index numarası 24 çıkar. Bu index numarası bize 24.indexten itibaren bu kelimenin 
# verilen cümle içinde olduğunu söyler.
#Pozitif bir sayı olursa kelime cümle içinde mevcuttur ama negatif bir sayı olursa
#cümlede o kelime yoktur.

# isFound = message.startswith('H')
# print(isFound)
# True sonucu gelir.Mesajın H ile başladığını gösterir.


isFound = message.endswith('H')
print(isFound)
# False sonucu gelir.Mesaj H ile bitmiyor.  # . ile bitiyor.

# message = message.replace('Sıla','Esra')
# print(message)
# Mesaj içerinde Sıla bilgisini bulur ve yerine Esra'yı koyarak mesajı yazdırır.
# message = message.replace(' ','*')
# print(message)
# Boşluk karakterlerini bul ve yerine * ekle.
# message = message.replace(' ç','c').replace('S','e').replace('H','n')
# print(message)
# #.replace yaparak devam ettirebilirsin.

# message = message.center(100)
# print(message) 
# Vermiş olunan string bilgisini 100 karakterlik bilgi içerisine alır.
# Sağ ve soldan eşit boşluklar bırakılır ve mesaj ortalanır.

message = message.center(50,'*')
print(message) 
# Sağda ve solda eşit sayıda * var ve tüm karakterler toplamı 50 oluyor.