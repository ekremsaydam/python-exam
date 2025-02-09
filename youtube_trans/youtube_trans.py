from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter
from youtube_transcript_api._errors import TranscriptsDisabled

video_id = "C95drFKy4ss"

try:
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    formatter = TextFormatter()
    documents = formatter.format_transcript(transcript)
    print(documents)
except TranscriptsDisabled:
    print(f"Hata: {video_id} ID'li video için altyazılar devre dışı bırakılmış.")
except Exception as e:
    print(f"Beklenmeyen bir hata oluştu: {str(e)}")

# https://github.com/jdepoix/youtube-transcript-api
