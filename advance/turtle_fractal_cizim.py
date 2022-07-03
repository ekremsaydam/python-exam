"""Turtle ile calismak karmaşık(Fractal) şekiller."""
from turtle import Turtle, Screen
cizim = {20: ['yellow', 'magenta', 'red', '#FFF8DC'],
         40: ['lightgreen', 'red', 'yellow', '#FFF8DC'],
         60: ['cyan', 'yellow', 'magenta', '#FFF8DC']}


def ciz(uzunluk: int, renk: str, carpan: int) -> None:
    """Karmaşık düzenli çizim.

    Args:
        uzunluk (int): çizgi uzunluğu
        renk (str): çizgi rengi
        carpan (int): karmaşıklık çarpanı
    """
    if uzunluk < 10:
        return None
    else:
        t.pensize(2)
        t.pencolor(renk)
        t.forward(uzunluk)
        t.left(30)
        ciz(carpan*uzunluk/(carpan+1), renk, carpan)
        t.right(60)
        ciz(carpan*uzunluk/(carpan+1), renk, carpan)
        t.left(30)
        t.backward(uzunluk)


t = Turtle()  # Turtle object
s = Screen()  # Screen Object

s.bgcolor('black')
# tracer : Çizim animasyonunu açar/kapatır ve
# güncelleme çizimleri için gecikmeyi duzenler
# s.tracer(False)
s.title('Fractal Tree Pattern')
t.speed(1000)
#################################
t.left(90)
ciz(20, 'yellow', 3)

t.right(90)
ciz(20, 'magenta', 3)

t.left(270)
ciz(20, 'red', 3)

t.right(90)
ciz(20, '#FFF8DC', 3)
#################################
ciz(40, 'lightgreen', 4)

t.right(90)
ciz(40, 'red', 4)

t.left(270)
ciz(40, 'yellow', 4)

t.right(90)
ciz(40, '#FFF8DC', 4)
#################################
ciz(60, 'cyan', 6)

t.right(90)
ciz(60, 'yellow', 6)

t.left(270)
ciz(60, 'magenta', 6)

t.right(90)
ciz(60, '#FFF8DC', 6)

s.exitonclick()
