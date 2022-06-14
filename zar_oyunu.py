"""zar oyunu."""
import random

min_deger = 1
max_deger = 6

tekrar_atilsin_mi = "evet"

while tekrar_atilsin_mi.upper() == "EVET" or tekrar_atilsin_mi.upper() == 'E':
    print("Zarlar atılıyor...")
    print("Değerler : ")
    print(random.randint(min_deger, max_deger))
    print(random.randint(min_deger, max_deger))

    tekrar_atilsin_mi = input("Tekrar zar atılsın mı [evet-e]: ")

