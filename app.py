from moviepy.editor import VideoFileClip, TextClip , CompositeVideoClip
import pysrt

def sub_to_seconds(sub):
    """将 SubRipTime 对象转换为秒数"""
    start = sub.start.hours * 3600 + sub.start.minutes * 60 + sub.start.seconds + sub.start.milliseconds / 1000
    end = sub.end.hours * 3600 + sub.end.minutes * 60 + sub.end.seconds + sub.end.milliseconds / 1000
    return start, end

def add_subtitles(video_path, subtitles_path, output_path):
    # 加载视频文件
    video = VideoFileClip(video_path)

    # 加载字幕文件
    subtitles = pysrt.open(subtitles_path)

    # 生成字幕剪辑
    txt_clips = [TextClip(txt=sub.text, font='Arial', fontsize=24, color='white')
                    .set_duration(end - start)
                    .set_position(('center', 0.8), relative=True)
                    .set_start(start)
                 for sub in subtitles
                 for start, end in [sub_to_seconds(sub)]]

    # 合并视频和字幕
    final_clip = CompositeVideoClip([video] + txt_clips)

    # 写入新的视频文件
    final_clip.write_videofile(output_path)

if __name__ == '__main__':
    video_path = 'ASurvey.webm'
    subtitles_path = 'ASurvey.srt'
    output_path = 'output.mp4'
    add_subtitles(video_path, subtitles_path, output_path)