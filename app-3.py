from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip
import pysrt

def sub_to_seconds(sub):
    """将 SubRipTime 对象转换为秒数"""
    start = sub.start.ordinal / 1000
    end = sub.end.ordinal / 1000
    return start, end

def adjust_font_size(video_width, text, max_width_ratio=0.8, font='STHeiti', initial_fontsize=24, min_fontsize=16):
    """根据视频宽度动态调整字体大小"""
    fontsize = initial_fontsize
    txt_clip = TextClip(txt=text, font=font, fontsize=fontsize, color='white')
    while txt_clip.size[0] > video_width * max_width_ratio and fontsize > min_fontsize:
        fontsize -= 1
        txt_clip = TextClip(txt=text, font=font, fontsize=fontsize, color='white')
    return fontsize

def add_subtitles(video_path, subtitles_path, output_path, font='STHeiti', font_color='yellow', stroke_color='black', stroke_width=0, bg_color='black'):
    video = VideoFileClip(video_path)
    video_duration = min(video.duration, 98)  # 获取视频实际长度，最多为98秒
    video = video.subclip(0, video_duration)
    
    video_width = video.size[0]  # 获取视频宽度
    subtitles = pysrt.open(subtitles_path, encoding='utf-8')
    clips = [video]  # 包含原始视频的列表

    for sub in subtitles:
        start, end = sub_to_seconds(sub)
        if start < video_duration:
            end = min(end, video_duration)  # 调整字幕时间，确保它们在视频的前100秒内
            fontsize = adjust_font_size(video_width, sub.text, font=font)
            # 创建带有背景的TextClip，去掉边框，未加粗（需要加粗字体支持）
            txt_clip_bg = TextClip(txt=sub.text, font=font, fontsize=fontsize, color=font_color, stroke_color=stroke_color, stroke_width=0, bg_color=bg_color)
            txt_clip_bg = txt_clip_bg.set_duration(end - start).set_position(('center', 'bottom')).set_start(start)
            clips.append(txt_clip_bg)  # 将带背景的字幕剪辑添加到列表中

    # 使用原始视频的音频合成最终剪辑
    final_clip = CompositeVideoClip(clips)
    final_clip.audio = video.audio
    try:
        final_clip.write_videofile(output_path, codec='libx264', audio_codec='aac')
    except:
        print("ERROR")

if __name__ == '__main__':
    video_path = 'ASurvey.webm'
    subtitles_path = 'ASurvey.srt'
    output_path = 'output.mp4'
    add_subtitles(video_path, subtitles_path, output_path)

