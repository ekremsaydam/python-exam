"""Sifre uretme."""
import random

kucuk_harfler = "".join([chr(x) for x in range(ord("a"), ord("z"))])
buyuk_harfler = kucuk_harfler.upper()
rakamlar = "".join(list(map(str, range(0, 10))))
semboller = "[]{}()+-*/.,;_-'\"`"
# print(kucuk_harfler)
# print(buyuk_harfler)
# print(rakamlar)
tumkarakterler = kucuk_harfler + buyuk_harfler + rakamlar + semboller
sifre_uzunlugu = 16
sifre = "".join(random.sample(tumkarakterler, sifre_uzunlugu))
print(sifre)
