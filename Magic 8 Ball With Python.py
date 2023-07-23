from random import choice

cevaplar = ["Evet", "Cevabı Yakın Bir Arkadaşın Verecek", "Cevap Hislerinde Gizli",
"Cevabı Hayır Ama Senin İçin Daha İyisi Olacak", "Kaçınılmaz Hayır",
"Bu Senin Kaderin", "Bugün Gökyüzündeki İşaretleri Takip Et, Cevap Orada",
"Bu Sana Bağlı"]
input("Cevabını Almak İstediğin Soruyu Sor:")
print("{}".format(choice(cevaplar)))
