"""rastgele hikaye oluşturma."""
import random


zaman = ['birkaç yıl önce', 'Dün', 'Dün gece',
         'Uzun zaman önce', 'Sabah', '15 Eylül\'de']
kim = ['bir tavşan', 'bir fil', 'bir fare', 'bir kaplumbağa', 'bir kedi']
isim = ['Ali', 'Hulk', 'Tony Stark', 'Sherlock']
yer = ['Türkiye\'de', 'Barselona\'da', 'Hindistan\'da',
       'Almanya\'da', 'Venedik\'de', 'İngiltere\'de']
gidilecekYerler = ['sinemaya', 'üniversiteye',
                   'seminere', 'okula', 'çamaşırhaneye']
olay = ['bir sürü arkadaş edindi.', 'bir hamburger yedi.',
        'gizli bir anahtar buldu.', 'bir gizemi çözdü.', 'bir kitap yazdı.']

print(random.choice(zaman),
      random.choice(kim),
      random.choice(yer), 'yaşarken',
      random.choice(gidilecekYerler), 'gitti',
      've', random.choice(olay))
