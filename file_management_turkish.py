
#! Dosya okuma "r" -> Dosya bulunması gerekir.

# dosya = open("planlar.txt","r",encoding="utf-8") #? Dosyayı açma. Türkçe karakterleri yazabilmek için "utf-8" kullanıyoruz.

# print(dosya.read()) #? Dosyayı okur ve ekrana yazdırır.
# print(dosya.read(50)) #? İçine yazılan değer kadar dosya karakterini okur ve ekrana yazdırır.
# print(dosya.readline()) #? Bulunduğumuz satırın hepsini okur ve ekrana yazdırır.
# print(dosya.readline(50)) #? İçine yazılan değer kadar o satırın karakterini okur ve ekrana yazdırır.
# print(dosya.readlines()) #? Tüm satırları okuyarak bir liste oluşturur, ve her satır bir eleman olur.
# print(dosya.tell()) #? İmlecimizin nerede olduğunu söyler.
# dosya.seek(5) #? İmlecimizin yerini değiştirir.

# dosya.close()

#----------------------------

#! Dosya yazma "w" -> Dosya yok ise otomatik oluşturur. (Üzerine yazar.)

# dosya = open("planlar.txt","w",encoding="utf-8")

# dosya.write("Hello") #? Dosyanın içine yazı yazar.
# dosya.writelines(["7:30 Kahvaltı\n","9:00 Koşu\n","11:00 Kitap Okuma\n"]) #? Her satır bir liste elemanını gösterecek şekilde yazı yazar.

# dosya.close()

#---------------------------

#! Dosya yazma "a" -> Dosya yok ise otomatik oluşturur. (Var olan yazıların en son satırına ve karakterine gidip yazma işlemine başlar.)

# dosya = open("planlar.txt","a",encoding="utf-8")

# dosya.write("12:00 Gezi\n") #? Dosyanın içine yazı yazar.

# dosya.close()

#-------------------------

#! Dosyaları bu şekilde de kullanabiliriz. (İşlem bittikten sonra dosyalar otomatik olarak kapanır.)

# with open("planlar.txt","w",encoding="utf-8") as dosya:
#    dosya.write("14:00 Kitap Okumak\n")
#    dosya.writelines(["15:00 Yüzme dersi\n","16:00 Koşu\n"])
