"""PNG dosyasını JPG ye dönüştürmek."""
from os import path as pt
import tkinter as tk
from tkinter import filedialog
from PIL import Image


root = tk.Tk()
canvas = tk.Canvas(root, width=300, height=250,
                   bg='azure3', relief='raised')
canvas.pack()

label1 = tk.Label(root, text='Resim Donusturucu', bg='azure3')
label1.config(font=('helvetica', 20))
canvas.create_window(150, 60, window=label1)
IMG, IMG_PATH = None, None


def get_png():
    """PNG yi yükler."""
    global IMG, IMG_PATH
    IMG_PATH = filedialog.askopenfilename(defaultextension='.png',
                                          filetypes=[('PNG File',
                                                      '.png')])
    if IMG_PATH is not None and\
            pt.exists(IMG_PATH):
        IMG = Image.open(IMG_PATH)


btn_browse_png = tk.Button(text='PNG dosyası seç', command=get_png,
                           bg='royalblue', fg='white',
                           font=('helvetica', 12, 'bold'))
canvas.create_window(150, 130, window=btn_browse_png)


def convert():
    """PNG yi JPG dönüştürmek."""
    global IMG, IMG_PATH
    if IMG is not None:
        export_file_full_path = filedialog.asksaveasfilename(
            defaultextension='.jpg',
            filetypes=[('JPG file', '.jpg .jpeg')])
        if export_file_full_path is not None and\
                export_file_full_path != '' and\
                pt.exists(IMG_PATH):
            IMG.save(export_file_full_path)


btn_save = tk.Button(text='PNG yi JPG ye dönüştür', command=convert,
                     bg='royalblue', fg='white',
                     font=('helvetica', 12, 'bold'))
canvas.create_window(150, 180, window=btn_save)


root.mainloop()
