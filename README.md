# movieAddSubtitle

分享英文字幕翻译并加载回视频的全流程，总结一下具体操作流程：

1.  使用yt-dlp下载youtube上的视频，譬如：
```
yt-dlp -f 'bestvideo[ext=webm]+bestaudio[ext=webm]/best[ext=webm]' -o "ASurvey.%(ext)s" https://www.youtube.com/watch?v=MnrJzXM7a6o
```

2. 使用whisper进行字幕抽取，譬如：

```
[推荐] whisper ASurvey.webm --task translate --language Chinese --model small --fp16 False
[或者] whisper ASurvey.webm --initial_prompt "以下是普通话的句子。" --language Chinese --model small  --fp16 False
```
3. 使用ChatGPT将生成的srt文件进行翻译.

4-1. 使用moviepy进行字幕重新加载回视频，生成新视频output.mp4
 - https://github.com/zgimszhd61/movieAddSubtitle

4-2. 更好的选择是使用capcut来进行导入和重新生成视频.


