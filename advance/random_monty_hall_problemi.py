"""Oyun. Monty Hall Problemi.
Bir yarışma programında olduğunuzu ve üç kapıdan birini seçme hakkınız
olduğunu varsayalım. Kapılardan birinin ardında bir araba, diğerlerinin
ardında ise keçiler var. Kapılardan birini, diyelim ki 1'inciyi seçiyorsunuz
ve kapıların ardında ne olduğunu bilen sunucu, diğer kapılardan birini,
diyelim ki ardında keçi olan 3'üncüyü açıyor. Daha sonra size soruyor:
"2. kapıyı seçmek ister misiniz?" Seçiminizi değiştirmek sizin
yararınıza mıdır?
"""
from numpy import random


def oyun(kazanankapi, secilenkapi, degisim=False):
    """Seçilen ve kazanan kapı dışındaki bir kapıyı seçip göstermek."""
    # assert kazanankapi < 3
    # assert kazanankapi >= 0

    cikarilankapi = next(i for i in range(3)
                         if i != secilenkapi and i != kazanankapi)
    if degisim:
        secilenkapi = next(i for i in range(3)
                           if i != secilenkapi and i != cikarilankapi)
    return secilenkapi == kazanankapi


if __name__ == '__main__':
    # oyun_kapilari = numpy.random.random_integers(0, 2, 1000**2)
    oyun_kapilari = random.randint(0, 2+1, 1000**2)
    kazanan_kapi = [d for d in oyun_kapilari if oyun(1, d)]
    print("Seçimi değiştirmeden kazanma yüzdesi : ",
          len(kazanan_kapi) / len(oyun_kapilari))

    kazanan_kapi = [d for d in oyun_kapilari if oyun(1, d, degisim=True)]
    print('Seçimi değiştirdiğinde kazanma yüzdesi :',
          len(kazanan_kapi)/len(oyun_kapilari))
