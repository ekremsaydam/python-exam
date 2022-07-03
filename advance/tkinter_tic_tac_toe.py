"""Tic-Tac-Toe"""
import tkinter as tk
import numpy as np

OYUN_ALANI_BOYUTU = 600
SEMBOL_BOYUTU = (OYUN_ALANI_BOYUTU / 3 - OYUN_ALANI_BOYUTU/10)/2

SEMBOL_KALINLIGI = 50
X_SEMBOL_RENGI = '#EE4035'
O_SEMBOL_RENGI = '#0492CF'
YESIL_RENK = '#7BC043'

X_DEGER = -1
O_DEGER = 1


class TicTacToe():
    """TicTacToe"""

    def click(self, event: tk.Event):
        """Tıklandığında konum bilgilerin al."""
        grid_piksel_konumu = [event.x, event.y]
        mantiksal_konum = self.grid_pikselden_mantiksal_konuma(
            grid_piksel_konumu)
        # print(mantiksal_konum)
        # self.ciz(mantiksal_konum, 'O', O_SEMBOL_RENGI)

        if not self.oyun_tahtasi_tekrarlansin_mi:
            if not self.oyun_tahtasi_isaretli_mi(mantiksal_konum):
                if self.x_oyuncu:
                    self.ciz(mantiksal_konum, 'X', X_SEMBOL_RENGI)
                    self.oyun_tahtasi[mantiksal_konum[1]
                                      ][mantiksal_konum[0]] = X_DEGER
                else:
                    self.ciz(mantiksal_konum, 'O', O_SEMBOL_RENGI)
                    self.oyun_tahtasi[mantiksal_konum[1]
                                      ][mantiksal_konum[0]] = O_DEGER
                self.x_oyuncu = not self.x_oyuncu

            print(self.oyun_tahtasi)
            if self.oyun_bitti_mi():
                self.oyun_bitis_ekrani()
                print('Bitti')
        else:
            self.canvas.delete('all')
            self.tekrar_oyna()
            self.oyun_tahtasi_tekrarlansin_mi = False

    def kazandi_mi(self, oyuncu):
        """Kazanan oyuncu olupolmadığının kontrolü."""
        oyuncu = X_DEGER if oyuncu == 'X' else O_DEGER
        print(oyuncu)
        # oyun_tahtasi kontrol
        # satır kontrol
        for i in range(3):
            print('icerik:', self.oyun_tahtasi[i][0],
                  self.oyun_tahtasi[i][1], self.oyun_tahtasi[i][2], oyuncu)
            if self.oyun_tahtasi[i][0] == self.oyun_tahtasi[i][1] ==\
                    self.oyun_tahtasi[i][2] == oyuncu:
                return True
            # sütün kontrol
            elif self.oyun_tahtasi[0][i] == self.oyun_tahtasi[1][i] ==\
                    self.oyun_tahtasi[2][i] == oyuncu:
                return True
        # çapraz kontrol
            elif self.oyun_tahtasi[0][0] == self.oyun_tahtasi[1][1] ==\
                    self.oyun_tahtasi[2][2] == oyuncu:
                return True
            elif self.oyun_tahtasi[0][2] == self.oyun_tahtasi[1][1] ==\
                    self.oyun_tahtasi[2][0] == oyuncu:
                return True

        return False

    def beraberlik_var_mi(self):
        """Beraberlik kontrol."""
        r, c = np.where(self.oyun_tahtasi == 0)
        print("Beraberlik kontrol : ", r, c)
        berabere = False
        if len(r) == 0:
            berabere = True

        return berabere

    def oyun_bitti_mi(self):
        """Oyun bitti mi?
        Ya birisi kazanmıştır yada oyun tahtası dolmuştur.
        """
        self.x_kazandi_mi = self.kazandi_mi('X')
        if not self.x_kazandi_mi:
            self.o_kazandi_mi = self.kazandi_mi('O')

        if not self.o_kazandi_mi:
            self.berabere_mi = self.beraberlik_var_mi()

        oyun_bitti = self.x_kazandi_mi or self.o_kazandi_mi or self.berabere_mi
        if self.x_kazandi_mi:
            print('X kazandı.')
        elif self.o_kazandi_mi:
            print('O kazandı.')
        elif self.berabere_mi:
            print('Berabere.')
        return oyun_bitti

    def initialize_board(self):
        """Oyun alanı yükleme."""
        for i in range(1, 3):
            self.canvas.create_line(
                i * OYUN_ALANI_BOYUTU/3, 0,
                i*OYUN_ALANI_BOYUTU/3,
                OYUN_ALANI_BOYUTU)

        for i in range(1, 3):
            self.canvas.create_line(
                0, i*OYUN_ALANI_BOYUTU/3,
                OYUN_ALANI_BOYUTU,
                i*OYUN_ALANI_BOYUTU/3)

    def __init__(self) -> None:
        self.window = tk.Tk()
        self.window.title('Tic-Tac-Toe')
        self.canvas = tk.Canvas(
            self.window, width=OYUN_ALANI_BOYUTU, height=OYUN_ALANI_BOYUTU)
        self.canvas.pack()

        self.window.bind('<Button-1>', self.click)

        self.initialize_board()
        self.x_oyuncu = True
        self.oyun_tahtasi = np.zeros(shape=(3, 3))
        print(self.oyun_tahtasi)

        self.x_oyuncu_baslasin_mi = True
        self.oyun_tahtasi_tekrarlansin_mi = False
        self.oyun_bitti = False

        self.x_kazandi_mi = False
        self.o_kazandi_mi = False
        self.berabere_mi = False

        self.x_skor = 0
        self.o_skor = 0
        self.berabere_skor = 0

    def mainloop(self):
        """mainloop tkinder."""
        self.window.mainloop()

    def grid_pikselden_mantiksal_konuma(self, grid_piksel_konum: int):
        """piksel konumundan mantiksal konuma."""
        grid_piksel_konum = np.array(grid_piksel_konum)
        return np.array(grid_piksel_konum//(OYUN_ALANI_BOYUTU/3), dtype=int)

    def mantiksaldan_grid_piksel_konumuna(self, mantiksal_konum: int):
        """mantıksal konumdan piksel konuma."""
        mantiksal_konum = np.array(mantiksal_konum, dtype=int)
        return (OYUN_ALANI_BOYUTU/3)*mantiksal_konum+OYUN_ALANI_BOYUTU/6

    def oyun_tahtasi_isaretli_mi(self, mantiksal_konum):
        """Oyun tahtasi"""
        if self.oyun_tahtasi[mantiksal_konum[1]][mantiksal_konum[0]] == 0:
            return False
        else:
            return True

    def ciz(self, mantiksal_konum, sekil, sembol_rengi):
        """Cizim."""
        # mantiksal_konum: grid deki yeri
        # grid_pozisyonu: pixel değeri
        mantiksal_konum = np.array(mantiksal_konum)
        grid_piksel_konum = self.mantiksaldan_grid_piksel_konumuna(
            mantiksal_konum)

        if sekil == 'O':
            self.canvas.create_oval(
                grid_piksel_konum[0]-SEMBOL_BOYUTU,
                grid_piksel_konum[1]-SEMBOL_BOYUTU,
                grid_piksel_konum[0]+SEMBOL_BOYUTU,
                grid_piksel_konum[1]+SEMBOL_BOYUTU,
                width=SEMBOL_KALINLIGI,
                outline=sembol_rengi)
        elif sekil == 'X':
            self.canvas.create_line(
                grid_piksel_konum[0]-SEMBOL_BOYUTU,
                grid_piksel_konum[1]-SEMBOL_BOYUTU,
                grid_piksel_konum[0]+SEMBOL_BOYUTU,
                grid_piksel_konum[1]+SEMBOL_BOYUTU,
                width=SEMBOL_KALINLIGI,
                fill=sembol_rengi)

            self.canvas.create_line(
                grid_piksel_konum[0]-SEMBOL_BOYUTU,
                grid_piksel_konum[1]+SEMBOL_BOYUTU,
                grid_piksel_konum[0]+SEMBOL_BOYUTU,
                grid_piksel_konum[1]-SEMBOL_BOYUTU,
                width=SEMBOL_KALINLIGI,
                fill=sembol_rengi)

    def oyun_bitis_ekrani(self):
        """oyun bitis ekranı."""
        if self.x_kazandi_mi:
            self.x_skor += 1
            txt = "KAZANAN: Oyuncu 1 (X)"
            renk = X_SEMBOL_RENGI
        elif self.o_kazandi_mi:
            self.o_skor += 1
            txt = "KAZANAN: Oyuncu 2 (O)"
            renk = O_SEMBOL_RENGI
        elif self.berabere_mi:
            self.berabere_skor += 1
            txt = "BERABERE!"
            renk = 'grey'
        self.canvas.delete('all')
        self.canvas.create_text(OYUN_ALANI_BOYUTU/2,
                                OYUN_ALANI_BOYUTU/3,
                                font='helvetiva 30 bold',
                                fill=renk, text=txt)
        skor_yazisi = 'Skorlar\n'
        self.canvas.create_text(OYUN_ALANI_BOYUTU/2,
                                5*OYUN_ALANI_BOYUTU/8,
                                font='helvetiva 30 bold', fill=renk,
                                text=skor_yazisi)
        skor_yazisi = 'Oyuncu 1 (X) : '+str(self.x_skor)+'\n'
        skor_yazisi += 'Oyuncu 2 (O) : '+str(self.o_skor)+'\n'
        skor_yazisi += 'Beraberlik : '+str(self.berabere_skor)
        self.canvas.create_text(OYUN_ALANI_BOYUTU/2,
                                3*OYUN_ALANI_BOYUTU/4,
                                font='helvetiva 15 bold',
                                fill=renk,
                                text=skor_yazisi)
        self.oyun_tahtasi_tekrarlansin_mi = True
        skor_yazisi = 'Tekrar oynayalım mı?\n'
        self.canvas.create_text(OYUN_ALANI_BOYUTU/2,
                                15*OYUN_ALANI_BOYUTU/16,
                                font='helvetica 30 bold',
                                fill='gray',
                                text=skor_yazisi)

    def tekrar_oyna(self):
        """Tekrar oynanan oyunun yüklenmesi."""
        self.initialize_board()
        self.x_oyuncu_baslasin_mi = not self.x_oyuncu_baslasin_mi
        # self.x_oyuncu_dondursun_mi = self.x_oyuncu_baslasin_mi
        self.oyun_tahtasi = np.zeros(shape=(3, 3))


game_instance = TicTacToe()
game_instance.mainloop()
