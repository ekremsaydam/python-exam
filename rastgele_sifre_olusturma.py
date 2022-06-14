"""rastgele sifre olusturma."""
import random
k = "abcdefghıijklmnoöpqrsştuüvwyz01234567890ABCDEFGHIİJKLMNOÖPQRSŞTUÜVWYZ!^+%&/([])*?"
uzunluk = input("Şifre kaç karakterden oluşmalıdır : ")
uzunluk_int = int(uzunluk) if uzunluk.isdecimal() else 0

SIFRE = "".join(random.sample(k, uzunluk_int))
print(SIFRE)
