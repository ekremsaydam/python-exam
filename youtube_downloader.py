"""Youtube downloader."""
from pytube import YouTube


def youtube_indir(url: str, /, *, only_audio: bool = True,
                  highest_resolution: bool = False, info: bool = False):
    """Youtube indirme programı."""
    def indir(secim_sor=True, secim=None):
        if secim_sor:
            secim = input("itag Seçiminiz : ")
        if secim is not None and secim.isdecimal():
            secilen = video.streams.get_by_itag(secim)
            if secilen is not None:
                print(secilen)
                secilen.download()
            else:
                print("Hatalı itag girişi.")
        else:
            print("Lütfen sayısal bir değer giriniz.")

    video = YouTube(url)
    if info:
        print("Videonun Başlığı :", video.title)
        print("İzlenme Sayısı: ", video.views)
        print("Video Uzunluğu :", video.length)
        print("Video Açıklaması :", video.description)
        print("Beğeni durumu :", video.rating)
    if only_audio:
        for audio in video.streams.filter(only_audio=True):
            print(audio)
        indir()
    else:
        match highest_resolution:
            case True:
                print(video.streams.get_highest_resolution())
                video.streams.get_highest_resolution().download()
            case False:
                for icerik in video.streams.filter(progressive=True):
                    print(icerik)
                for icerik in video.streams.filter(adaptive=True):
                    print(icerik)

                indir()


youtube_indir(
    'https://www.youtube.com/watch?v=KoXxD99BYDw&list=PLfWSsla4-3s0OgIyZpCb8UVzkvJcTzw9B', only_audio=False, info=True)
