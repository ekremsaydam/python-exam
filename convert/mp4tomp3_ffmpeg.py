import subprocess

# videofile = "onnumara.mp4"
audiofile = "example.mp4"
outputfile = "example.mp3"
# codec = "copy"
codec = "mp3"
# subprocess.run(f"ffmpeg -i {videofile} -i {audiofile} -c {codec} {outputfile}")
subprocess.run(f"ffmpeg -i {audiofile} -c {codec} {outputfile}")
