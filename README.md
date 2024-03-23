# movieAddSubtitle

分享英文字幕翻译并加载回视频的全流程，总结一下具体操作流程：

1.  使用yt-dlp下载youtube上的视频，譬如：

yt-dlp https://youtube.com/watch?v=ahnGLM-RC1Y

2. 使用whisper进行字幕抽取，譬如：

whisper A\ Survey\ of\ Techniques\ for\ Maximizing\ LLM\ Performance\ \[ahnGLM-RC1Y\].webm --task translate --language Chinese --model small

3. 使用ChatGPT将生成的srt文件进行翻译.

4. 使用moviepy进行字幕重新加载回视频，生成新视频output.mp4

https://github.com/zgimszhd61/movieAddSubtitle

整个过程中，moviepy的运行时间比较久（可能是我电脑比较烂的原因），花了4个小时，需要有点耐心。

请教各位大佬们这个过程什么地方可以加速，

有没有更好的办法？
