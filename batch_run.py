import os
print("your Youtube Address:")
youtbAddr = input()
## https://www.youtube.com/watch?v=MnrJzXM7a6o
os.system("yt-dlp -o 'ASurvey.%(ext)s' " + youtbAddr)
##os.system("whisper ASurvey.webm --task translate --language Chinese --model small --fp16 False")
os.system("whisper ASurvey.webm --task transcribe --language English --model small --fp16 False")
os.system("python3 app.py")
