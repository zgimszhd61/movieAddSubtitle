import os

os.system("yt-dlp -o 'ASurvey.%(ext)s' https://www.youtube.com/watch?v=MnrJzXM7a6o")
os.system("whisper ASurvey.webm --task translate --language Chinese --model small")
os.system("python3 app.py")
