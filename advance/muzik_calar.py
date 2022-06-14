"""Müzik Çalar Uygulaması."""
import tkinter as tkr  # pip install tk
from tkinter.filedialog import askdirectory
import os
import pygame  # pip install pygame


muzik_calar = tkr.Tk()
muzik_calar.title("Muzik Çalar")
muzik_calar.geometry("450x350")
klasor = askdirectory()
os.chdir(klasor)
muzik_listesi = os.listdir()

calma_listesi = tkr.Listbox(
    muzik_calar, font="Helvetica 12 bold", bg="yellow", selectmode=tkr.SINGLE)

for item in muzik_listesi:
    if item.endswith(('.mp3','.mp4')):
        POS = 0
        calma_listesi.insert(POS, item)
        POS += 1

pygame.init()
pygame.mixer.init()


def play():
    """müzik çal."""
    pygame.mixer.music.load(calma_listesi.get(tkr.ACTIVE))
    # a = set(calma_listesi.get(tkr.ACTIVE))
    pygame.mixer.music.play()


def stop():
    """Muzik durdur."""
    pygame.mixer.music.stop()


def pause():
    """Muzik duraklat."""
    pygame.mixer.music.pause()


def unpause():
    """Duraklatılmış müziği devam ettir."""
    pygame.mixer.music.unpause()


Button1 = tkr.Button(muzik_calar, width=5, height=3, font="Helvetica 12 bold",
                     text="PLAY", command=play, bg="blue", fg="white")
Button2 = tkr.Button(muzik_calar, width=5, height=3, font="Helvetica 12 bold",
                     text="STOP", command=stop, bg="red", fg="white")
Button3 = tkr.Button(muzik_calar, width=5, height=3, font="Helvetica 12 bold",
                     text="PAUSE", command=pause, bg="purple", fg="white")
Button4 = tkr.Button(muzik_calar, width=5, height=3, font="Helvetica 12 bold",
                     text="UNPAUSE", command=unpause, bg="orange", fg="white")

strvar = tkr.StringVar()
muzik_basligi = tkr.Label(
    muzik_calar, font="Helvetica 12 bold", textvariable=strvar)

muzik_basligi.pack()
Button1.pack(fill="x")
Button2.pack(fill="x")
Button3.pack(fill="x")
Button4.pack(fill="x")
calma_listesi.pack(fill="both", expand="yes")
muzik_calar.mainloop()
