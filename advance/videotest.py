from moviepy.editor import VideoFileClip
myclip = VideoFileClip('j2.mp4')
print([frame[0, :, 0].max()
       for frame in myclip.iter_frames()])
