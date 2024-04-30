# 安装yt-dlp和ffmpeg
!pip install yt-dlp
!apt install ffmpeg

# 使用yt-dlp下载指定YouTube视频的音频，并将其转换为webm格式
!yt-dlp -x --audio-format mp3 https://www.youtube.com/watch?v=a7mS9ZdU6k4 -o 'Steve_Jobs_iPhone_Introduction_2007.%(ext)s'

# 安装Whisper
# !pip install git+https://github.com/openai/whisper.git

# 安装ffmpeg，这是一个音视频处理工具，Whisper在处理音频文件时需要用到
# !sudo apt update && sudo apt install ffmpeg
# !PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True
# !kill -9 47871
# 导入Whisper模块
import whisper
import torch
import os
torch.cuda.empty_cache()
os.environ['PYTORCH_CUDA_ALLOC_CONF'] = 'expandable_segments:True'

# 确保使用GPU加速
device = "cuda" if torch.cuda.is_available() else "cpu"

# 加载模型，这里使用的是中等大小的模型，并指定使用GPU
model = whisper.load_model("medium", device=device)

# 加载音频文件，这里假设音频文件名为"Steve_Jobs_iPhone_Introduction_2007.mp3"，并且已经上传到Colab的工作环境中
audio = whisper.load_audio("Steve_Jobs_iPhone_Introduction_2007.mp3")

# 调整音频长度到10秒
# audio = audio[:model.sample_rate * 10]

audio = whisper.pad_or_trim(audio)


# 将音频文件转换为梅尔频谱图，这是Whisper处理的第一步
mel = whisper.log_mel_spectrogram(audio).to(model.device)

# 设置解码选项，这里假设音频文件是英语的，并指定翻译任务
options = whisper.DecodingOptions(task="translate", language="zh", without_timestamps=False)

# 进行语音识别和翻译，得到结果
result = whisper.decode(model, mel, options)

# 打印识别出的文本
print(result.text)

