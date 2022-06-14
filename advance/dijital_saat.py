from tkinter import Label, Tk
import time

app_window = Tk()
app_window.title("Dijital Saat")
app_window.geometry("420x150")
app_window.resizable(1, 1)

text_font = ("Boulder", 68, "bold")
arkaplan = "#f2e750"
yazirengi = "#363529"
border_width = 25

label = Label(app_window, font=text_font, bg=arkaplan,
              fg=yazirengi, bd=border_width)
label.grid(row=0, column=1)


def digital_clock():
    anlik_zaman = time.strftime('%H:%M:%S')
    label.config(text=anlik_zaman)
    label.after(200, digital_clock)


digital_clock()
app_window.mainloop()
