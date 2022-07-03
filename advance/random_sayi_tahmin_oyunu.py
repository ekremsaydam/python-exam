import random
# 1 ile 100 arasında 1 ve 100 dahil
tutulan_sayi = random.randrange(1, 100)
girilen_sayi = -1
while tutulan_sayi != girilen_sayi:
    girilen_sayi = int(input("Lütfen bir sayı giriniz : "))

    if girilen_sayi < tutulan_sayi:
        print("YUKARI")
    elif girilen_sayi > tutulan_sayi:
        print("AŞAĞI")
    elif girilen_sayi == tutulan_sayi:
        print("Tebrikler. Bildiniz.")
        break
print("Programdan Çıkılıyor...")
