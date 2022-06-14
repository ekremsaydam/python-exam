"""Video dan metin çıkarmak."""
import time
import speech_recognition as sr  # pip install SpeechRecognition
import moviepy.editor as mp  # pip install moviepy
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
import ffmpeg  # pip install ffmpeg-python
# from pprint import pprint # json formatında anlaşılabilir gösterim.


DOSYA = "AkdenizUniversitesi2021.mp4"
DIL = 'tr'
PARCA_UZUNLUGU = 10 # 10 saniyelik parçalar halinde metine dönüştürme.

video_uzunlugu = float(ffmpeg.probe(DOSYA)['streams'][0]['duration'])
parca_video_sayisi = (video_uzunlugu // PARCA_UZUNLUGU)+1\
    if (video_uzunlugu // PARCA_UZUNLUGU) != (video_uzunlugu / PARCA_UZUNLUGU)\
    else (video_uzunlugu // PARCA_UZUNLUGU)
video_sayisi = int(parca_video_sayisi * PARCA_UZUNLUGU)
print(f"Bu video {video_sayisi} uzunluğunda")

vsay = list(range(0, video_sayisi+1, PARCA_UZUNLUGU))
# print(vsay)
diz = {}
for i in range(len(vsay)-1):
    ffmpeg_extract_subclip(
        DOSYA,
        vsay[i]-2*(vsay[i] != 0),
        vsay[i+1],
        targetname=fr"parcala\video_p{i+1}.mp4")

    clip = mp.VideoFileClip(fr"parcala\video_p{i+1}.mp4")
    clip.audio.write_audiofile(fr"parcala\ses_p{i+1}.wav")
    r = sr.Recognizer()
    audio = sr.AudioFile(fr"parcala\ses_p{i+1}.wav")
    with audio as source:
        # r.adjust_for_ambient_noise(source, duration=0.5)
        audio_file = r.record(source)
    try:
        RESULT = r.recognize_google(audio_file, language=DIL)
    except sr.UnknownValueError:
        RESULT = "ses anlaşılamadı."
    except sr.RequestError:
        RESULT = "Konuşma tanıma hizmeti hatası"
    diz[f'parca{i+1}'] = RESULT


vsay_parcalari = [(f"{time.strftime('%H:%M:%S', time.gmtime(i*PARCA_UZUNLUGU))} - " +
                   diz[f'parca{i+1}']) for i in range(len(diz))]
TEXT = '\n'.join(vsay_parcalari)

with open('video_metin.txt', mode='w', encoding="utf8") as file:
    file.write("Video İçeriği\n")
    file.write(TEXT)
    print('Finally ready!')
