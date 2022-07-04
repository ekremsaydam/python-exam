"""Web sitesi içerisinden bilgi çekmek."""
import requests
from bs4 import BeautifulSoup  # pip install beautifulsoup4
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/
import pandas as pd
import csv

# url = 'https://www.tripadvisor.in/Hotels-g28932-Hawaii-Hotels.html'
url = 'https://www.tripadvisor.com.tr/Hotels-g293969-Turkey-Hotels.html'
user_agent = ({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
                              AppleWebKit/537.36 (KHTML, like Gecko) \
                              Chrome/90.0.4430.212 Safari/537.36',
               'Accept-Language': 'en-US, en;q=0.5'
               })

otel_isimleri = []


def sayfa_icerigini_al(url_bilgisi):
    """url ile belirtilen html bilgisni alır."""
    page = requests.get(url_bilgisi, headers=user_agent)
    # Diğer parserlar hakkında bilgi.
    # https://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-a-parser
    return BeautifulSoup(page.text, features='html.parser')


soup = sayfa_icerigini_al(url)
for otel_ismi in soup.findAll('div', {'class': 'listing_title'}):
    otel_isimleri.append(" ".join(str(otel_ismi.text).split()[1:]))

derecelendirme = []
for derece in soup.findAll('a', {'data-clicksource': 'BubbleRating'}):
    derecelendirme.append(derece['alt'].strip())

yorumlar = []
for yorum in soup.findAll('a', {'class', 'review_count'}):
    yorumlar.append(yorum.text.strip())

fiyatlar = []
for fiyat in soup.findAll('div', {'class', 'price-wrap'}):
    # print(str(fiyat.text))
    fiyatlar.append(str(fiyat.text).rsplit('₺')[-1]+'₺')

veri = {'OTEL ISIMLERI': otel_isimleri,
        'DERECELENDIRME': derecelendirme,
        'YORUMLAR': yorumlar,
        'FIYATLAR': fiyatlar}

# dataframe oluşturma.
veri_ambari = pd.DataFrame.from_dict(veri)
print(veri_ambari.head(10))

veri_ambari.to_csv('oteller.csv', index=False, header=True)
