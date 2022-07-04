"""KG dönüştürme."""
from tkinter import END, Button, Entry, Label, StringVar, Text, Tk

my_form = Tk()
lbl_kg = Label(my_form, text='Ağırlığı KG olarak giriniz : ')

txt_kg_deger = StringVar()
txt_kg = Entry(my_form, textvariable=txt_kg_deger)

lbl_gram = Label(my_form, text='Gram')
txt_gram = Text(my_form, height=5, width=30)

lbl_pound = Label(my_form, text='Pound')
txt_pound = Text(my_form, height=5, width=30)

lbl_ounce = Label(my_form, text='Ounce')
txt_ounce = Text(my_form, height=5, width=30)


def donustur():
    """KG değerlerini farklı birimlere dönüştürme."""
    if txt_kg_deger.get().isdecimal():
        gram = float(txt_kg_deger.get())*1000
        pound = float(txt_kg_deger.get())*2.20462
        ounce = float(txt_kg_deger.get())*35.274

        txt_gram.delete('1.0', END)
        txt_gram.insert(END, gram)

        txt_pound.delete('1.0', END)
        txt_pound.insert(END, pound)

        txt_ounce.delete('1.0', END)
        txt_ounce.insert(END, ounce)


btn_donustur = Button(my_form, text='Dönüştür', command=donustur)

lbl_kg.grid(row=0, column=0)
txt_kg.grid(row=0, column=1)
lbl_gram.grid(row=1, column=0)
txt_gram.grid(row=2, column=0)
lbl_pound.grid(row=1, column=1)
txt_pound.grid(row=2, column=1)
lbl_ounce.grid(row=1, column=2)
txt_ounce.grid(row=2, column=2)
btn_donustur.grid(row=0, column=2)


my_form.mainloop()
