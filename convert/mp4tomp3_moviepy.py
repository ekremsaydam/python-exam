"""MP+ dosyasından MP3 elde etmek."""
from moviepy.editor import VideoFileClip

video = VideoFileClip("example.mp4")
audio = video.audio
audio.write_audiofile("example.mp3")
