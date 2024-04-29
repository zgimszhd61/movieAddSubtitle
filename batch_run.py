import os
youtbAddr = input()
## https://www.youtube.com/watch?v=MnrJzXM7a6o
os.system("yt-dlp -o 'ASurvey.%(ext)s' " + youtbAddr)
os.system("whisper ASurvey.webm --task translate --language Chinese --model small")
os.system("python3 app.py")
