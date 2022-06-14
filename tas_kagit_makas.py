"""Tas, kagit, makas oyunu."""
import random

secenekler = ["Taş", "Kağıt", "Makas"]
oyuncu_skor = 0
bilgisayar_skor = 0

while True:
    bilgisayar = random.choice(secenekler)
    oyuncu = input("Taş, Kağıt veya Makas ? : ").strip().capitalize()

    if oyuncu == bilgisayar:
        print("Berabere!")
    elif oyuncu == "Taş":
        if bilgisayar == "Kağıt":
            print("Kaybettiniz!", bilgisayar, oyuncu, "kaplar.")
            bilgisayar_skor += 1
        else:
            print("KAZANDINIZ!", oyuncu, bilgisayar, "parçalar.")
            oyuncu_skor += 1
    elif oyuncu == "Kağıt":
        if bilgisayar == "Makas":
            print("Kaybettiniz!", bilgisayar, oyuncu, "keser")
            bilgisayar_skor += 1
        else:
            print("KAZANDINIZ!", oyuncu, bilgisayar, "kaplar")
            oyuncu_skor += 1
    elif oyuncu == "Makas":
        if bilgisayar == "Taş":
            print("Kaybettiniz!", bilgisayar, oyuncu, "kaplar")
            bilgisayar_skor += 1
        else:
            print("KAZANDINIZ!", oyuncu, bilgisayar, "keser")
            oyuncu_skor += 1
    elif oyuncu == "Çıkış":
        print("Final Skoru:")
        print(f"Bilgisayar : {bilgisayar_skor}")
        print(f"Oyuncu : {oyuncu_skor}")
        break
