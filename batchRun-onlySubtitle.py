import os
print("input your Youtube Address")
youtbAddr = input()
## https://www.youtube.com/watch?v=MnrJzXM7a6o
os.system("rm -rf ASurvey.*")
os.system("yt-dlp -f 'bestvideo[ext=webm]+bestaudio[ext=webm]/best[ext=webm]' -o 'ASurvey.%(ext)s' " + youtbAddr)
os.system("whisper ASurvey.webm --task translate --language Chinese --model small --output_format srt")
