"""Vucut kitle indeksi."""
uzunluk = float(input("Boy uzunluğunuzu santimetre olarak giriniz : "))
agirlik = float(input("Ağırlığınızı kilogram olarak giriniz : "))
uzunluk /= 100
VKI = agirlik/(uzunluk**2)
print("Vücut Kitle İndeksiniz : ", VKI)

if VKI > 0:
    if VKI <= 16:
        print("Ciddi derecede zayıfsın")
    elif VKI <= 18.5:
        print("Zayıfsınız")
    elif VKI <= 25:
        print("Sağlıklısınız")
    elif VKI <= 30:
        print("Fazla kilolusunuz.")
    else:
        print("Aşırı kilolusun")
else:
    print("Lütfen geçerli bir değer giriniz.")
