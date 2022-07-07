"""Kart Oyunu."""
from random import shuffle

KART_TIPLER = ('maça', 'kupa', 'karo', 'sinek')
KART_DEGERLER = ('2', '3', '4', '5', '6', '7',
                 '8', '9', '10', 'vale', 'kız', 'Papaz', 'As')


class Kart:
    """Kart classı."""
    global KART_TIPLER
    global KART_DEGERLER

    def __init__(self, deger, tip) -> None:
        self.deger = deger
        self.tip = tip

    def __lt__(self, c2):
        if self.deger < c2.deger:
            return True
        elif self.deger == c2.deger:
            if self.tip < self.tip:
                return True
        return False

    def __gt__(self, c2):
        """Büyükse."""
        if self.deger > c2.deger:
            return True
        elif self.deger == c2.deger:
            if self.tip > c2.tip:
                return True
        return False


class CekilenKart:
    """Kart hazırlık."""

    def __init__(self, degerler, tipler) -> None:
        self.kartlar = []
        for deger in range(len(degerler)):
            for tip in range(len(tipler)):
                self.kartlar.append(Kart(deger, tip))

        shuffle(self.kartlar)

    def kart_cek(self):
        """Kart çekmek."""
        if len(self.kartlar) == 0:
            return

        return self.kartlar.pop()


class Oyuncu:
    """Oyuncu Sınıfı."""

    def __init__(self, isim) -> None:
        self.kazanma_sayisi = 0
        self.kart = None
        self.name = isim


class Oyun:
    """Oyun Objesi."""

    def __init__(self) -> None:
        oyuncu1 = input('Oyuncu 1 in ismini giriniz : ')
        oyuncu2 = input('Oyuncu 2 in ismini giriniz : ')

        self.cekilen_kartlar = CekilenKart(KART_DEGERLER, KART_TIPLER)
        self.oyuncu1 = Oyuncu(oyuncu1)
        self.oyuncu2 = Oyuncu(oyuncu2)

    def kazanan(self, kazanan: Oyuncu):
        """Kazananı ekrana yazdırır."""
        print(
            f"{kazanan.name} bu raundu kazandı. Toplam kazanma sayısı {kazanan.kazanma_sayisi} ")

    def goster(self, p1n: Oyuncu, p1c: Kart, p2n: Oyuncu, p2c: Kart):
        """Kartları gösterir."""
        print(f'{p1n.name} kartı {KART_TIPLER[p1c.tip]} {KART_DEGERLER[p1c.deger]} -' +
              f'{p2n.name} kartı {KART_TIPLER[p2c.tip]} {KART_DEGERLER[p2c.deger]}')

    def oyna(self):
        """Oyuna başlamak için."""
        kartlar = self.cekilen_kartlar
        print("Oyun Başladı.")
        while len(kartlar.kartlar) >= 2:
            print("Toplam kart sayısı : ",len(kartlar.kartlar))
            res = input("Oynamak için bir tuşa basınız (çıkış için q) :")
            if res.upper() == 'Q':
                break

            p1n = self.oyuncu1
            p1c = self.cekilen_kartlar.kart_cek()
            p2n = self.oyuncu2
            p2c = self.cekilen_kartlar.kart_cek()

            self.goster(p1n, p1c, p2n, p2c)

            if p1c > p2c:
                p1n.kazanma_sayisi += 1
                self.kazanan(p1n)
            else:
                p2n.kazanma_sayisi += 1
                self.kazanan(p2n)
        kazanan = self.kazanan_kim(self.oyuncu1, self.oyuncu2)

        print(f'Oyun bitti. {kazanan}')

    def kazanan_kim(self, p1: Oyuncu, p2: Oyuncu):
        """Kazananı belirle."""
        if p1.kazanma_sayisi > p2.kazanma_sayisi:
            return p1.name
        elif p1.kazanma_sayisi < p2.kazanma_sayisi:
            return p2.name

        return "Berabere!..."


oyun = Oyun()
oyun.oyna()
