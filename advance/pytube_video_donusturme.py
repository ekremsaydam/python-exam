"""Convert Audio."""
from os import name as osName, system as setCmd
import os
from pytube import YouTube as getVideo


def main():
    """Main program."""
    video_url = input('Youtube video URL bilgisini giriniz : ')

    video = getVideo(video_url)
    audio_name = video.streams.get_audio_only('mp4').download()

    audio_salt_name = audio_name.split('\\')[-1]
    audio_ren_name = (audio_salt_name.split('.')[0] +
                      '.mp3').replace(' ', '')

    if osName == 'nt':
        # path = getPath()+'\\'
        # dosyanın daha önce yaratılıp yaratılmadığı kontrolü
        if os.path.exists(audio_ren_name):
            setCmd(f'del {audio_ren_name}')
        audio_salt_name = '"'+audio_salt_name+'"'
        setCmd(f'ren {audio_salt_name} {audio_ren_name}')
    else:
        # path = getPath()+'/'
        setCmd(f'mv {audio_salt_name} {audio_ren_name}')


if __name__ == '__main__':
    main()
