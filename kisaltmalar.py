"Kısaltmalar oluşturma."

uzun = input("Kısaltması istenen kelimeyi giriniz : ")
KISALTMA = "".join([v[0].capitalize() for v in uzun.split(' ')])
print(KISALTMA)
