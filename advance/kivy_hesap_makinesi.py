"""Hesap Makinası Uygulaması."""
from kivy.app import App  # pip install Kivy
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button


class HesapMakinasi(App):
    """Uygulama ana objesi."""

    def build(self):
        """kivy için gerekli fonksiyon."""
        # widget ekledikçe satır satır eklesin aşağıya doğru
        # yukarıdan aşağıya ekleme
        root_widget = BoxLayout(orientation='vertical')
        # Sonuç ekranı
        hesap_ekrani = Label(text=' ', size_hint_y=0.75,
                             halign='right', font_size=50)

        def hesap_ekrani_boyutlandir(label, new_height):
            label.font_size = 0.5*label.height
        hesap_ekrani.bind(size=hesap_ekrani_boyutlandir)
        root_widget.add_widget(hesap_ekrani)

        grid_sayisal_klavye = GridLayout(cols=4, size_hint_y=2)
        klavye_tuslari = ('1', '2', '3', '+',
                          '4', '5', '6', '-',
                          '7', '8', '9', '.',
                          '0', '*', '/', '=')
        for tus in klavye_tuslari:
            grid_sayisal_klavye.add_widget(Button(text=tus))
        root_widget.add_widget(grid_sayisal_klavye)

        def tus_tiklandiginda_hesap_ekrani_etkilesimi(instance):
            hesap_ekrani.text += instance.text

        for tus in grid_sayisal_klavye.children[1:]:
            tus.bind(on_press=tus_tiklandiginda_hesap_ekrani_etkilesimi)

        def hesapla(instance):
            """hesap_ekrani kivy.label.text e ekli olan işlem hesaplari."""
            try:
                hesap_ekrani.text = str(eval(hesap_ekrani.text))
            except:
                hesap_ekrani.text = 'Syntax error!'
        grid_sayisal_klavye.children[0].bind(on_press=hesapla)

        temizleme_tusu = Button(text='Temizle', size_hint_y=None, height=100)

        def hesap_ekrani_temizle(instance):
            hesap_ekrani.text = ''

        temizleme_tusu.bind(on_press=hesap_ekrani_temizle)
        root_widget.add_widget(temizleme_tusu)

        return root_widget


HesapMakinasi().run()
