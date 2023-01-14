"""SQLite3 test."""
import sqlite3

conn = sqlite3.connect("expenses.db")
cur = conn.cursor()

MENU_MAIN = """
HARCAMA LİSTESİ
1. Harcama Ekleme
2. Harcama Listesini görüntüleme
"""

MENU_HARCAMA = """
KATEGORİ LİSTELEME
1. Tüm harcama listesini görüntüle
2. Harcamaları kategorilere göre görüntüle
"""
while True:
    print(MENU_MAIN)
    secim = int(input("Seçiminiz : "))

    if secim == 1:
        tarih = input("Harcama tarihini giriniz (YYYY-AA-GG): ")
        aciklama = input("Harcama açıklamasını giriniz: ")

        cur.execute("SELECT DISTINCT category FROM expenses")
        kategoriler = cur.fetchall()

        print("Kategoriler:")
        for idx, kategori in enumerate(kategoriler):
            print(f"{idx+1}. {kategori[0]}")
        print(f"{len(kategoriler)+1}. Yeni bir kategori oluştur.")

        kategori_secim = int(input("Kategori seçiminiz : "))
        if kategori_secim == len(kategoriler) + 1:
            kategori = input("Yeni kategori adını girin : ")
        else:
            kategori = kategoriler[kategori_secim - 1][0]

        harcama_miktari = input("Harcama miktarını giriniz : ")

        cur.execute(
            """INSERT INTO expenses (Date, description, category, price)
                       VALUES (?,?,?,?)""",
            (tarih, aciklama, kategori, harcama_miktari),
        )
        conn.commit()
    elif secim == 2:
        print(MENU_HARCAMA)

        harcama_goster = int(input("Seçiminiz : "))
        if harcama_goster == 1:
            cur.execute("SELECT * FROM expenses")
            harcamalar = cur.fetchall()
            for harcama in harcamalar:
                print(harcama)
        elif harcama_goster == 2:
            ay = input("Ay bilgisini giriniz (AA) : ")
            yil = input("Yıl bilgisini giriniz (YYYY) : ")
            cur.execute(
                """SELECT category, SUM(price) FROM expenses
                        WHERE strftime('%m', Date) = ? AND
                              strftime('%Y', Date) = ?
                        GROUP BY category""",
                (ay, yil),
            )

            harcamalar = cur.fetchall()
            for harcama in harcamalar:
                print(f"Category: {harcama[0]}, total: {harcama[1]}")
        else:
            exit()

    repeat = input("Başka işlem yapmak ister misiniz? (e/h) : \n")
    if repeat.lower() != "e":
        break

conn.close()
