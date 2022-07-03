"""Stres çarkı."""
from turtle import Turtle, Screen, done
t = Turtle()
s = Screen()
durum = {"donus": 0}


def dondur():
    """Carki dondur."""
    t.clear()
    aci = durum['donus']/10
    t.right(aci)
    t.width(20)
    t.forward(100)
    t.dot(120, 'red')
    t.back(100)
    t.right(120)
    t.forward(100)
    t.dot(120, 'green')
    t.back(100)
    t.right(120)
    t.forward(100)
    t.dot(120, 'blue')
    t.back(100)
    t.right(120)
    s.update()


def animate():
    """Cark animasyonu."""
    if durum['donus'] > 0:
        durum['donus'] -= 1

    dondur()
    s.ontimer(animate, 20)


def hizlandir():
    """Hızlandırma."""
    durum['donus'] += 10


# shape()
# form boyutları setup(genişlik,yükseklik,başlangıçx,başlangıçy)
s.setup(420, 420, 370, 0)

# tracer: Çizim animasyonunu açar/kapatır ve
# güncelleme çizimleri için gecikmeyi duzenler
s.tracer(False)
t.hideturtle()
s.onkey(hizlandir, 'space')
s.listen()
animate()
done()
