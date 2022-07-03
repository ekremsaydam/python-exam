"""Yazım denetimi."""
# pip install textblob
from textblob import TextBlob

hatali_kelimler = ["Data Scence", "Mahine Learnin"]
dogru_kelimeler = []

for hkelime in hatali_kelimler:
    dogru_kelimeler.append(str(TextBlob(hkelime).correct()))
print("Hatalı KElime Yazımları : ", hatali_kelimler)
print("Doğru kelime yazımları : ", dogru_kelimeler)
