"""Çalar saat."""
from datetime import datetime
# from tracemalloc import start
from playsound import playsound
# from os import startfile
# from pydub import AudioSegment,playback
alarm_zaman = input("Alarm zamanını giriniz [SS:DD:ss]: ")
alarm_saat = alarm_zaman.split(':')[0]
alarm_dakika = alarm_zaman.split(':')[1]
alarm_saniye = alarm_zaman.split(':')[2]
print("Alarm ayarlandi.")
GOSTER = 1
while True:
    suan = datetime.now()
    suan_saat = suan.strftime('%I')
    suan_dakika = suan.strftime('%M')
    suan_saniye = suan.strftime('%S')
    if GOSTER == 1:
        # print(suan)
        # print(suan_saat, suan_dakika, suan_saniye)
        # print(alarm_saat, alarm_dakika, alarm_saniye)
        GOSTER -= 1

    if (alarm_saat == suan_saat and
        alarm_dakika == suan_dakika and
            alarm_saniye <= suan_saniye):
        print("ALARM çalınıyor.")
        playsound('alarm2.mp3')
        # startfile('onnumara.mp3')
        # ses = AudioSegment.from_file("onnumara.mp4", "mp4")
        # playback.play(ses)
        print("Alarm sonlandırıldı.")
        break
