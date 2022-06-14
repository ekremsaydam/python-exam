"""mail adresi kullanici adi."""
email = input("lütfen email adresiniiz giriniz : ").strip()
elist = email.split('@') if '@' in email else []
kullaniciAdi = email[:email.index('@')]
domainName = email[email.index('@')+1:]
if len(elist) > 0:
    print(f"kullanıcı adınız {elist[0]} domain adresi {elist[1]}")

print(kullaniciAdi, domainName)
