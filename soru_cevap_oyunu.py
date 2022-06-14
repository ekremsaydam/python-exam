"""soru cevap oyunu."""


def cevap_kontrol(kullanici_cevap: str, dogru_cevap: str):
    devam = True
    deneme = 0
    global skor
    while devam and deneme < 3:
        if kullanici_cevap.lower() == dogru_cevap.lower():
            print("Doğru cevap")
            skor += 1
            devam = False
        else:
            if deneme < 2:
                kullanici_cevap = input(
                    "Üzgünüm Yanlış cevap, tekrar deneyiniz : ")
            deneme += 1

    if deneme == 3:
        print("Doğru cevap : ", dogru_cevap)


skor = 0
print("Hayvanlar Alemi")
soru1 = input("En hızlı kara hayvanı hangisidir? : ")
cevap_kontrol(soru1, "çita")
soru2 = input("Kuzey Kutbu'nda yaşayan ayı hangisidir? : ")
cevap_kontrol(soru2, "kutup ayısı")
soru3 = input("En büyük hayvan hangisidir? : ")
cevap_kontrol(soru3, "Mavi balina")

print("Skor", skor)
