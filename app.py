from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip
import pysrt

def sub_to_seconds(sub):
    """将 SubRipTime 对象转换为秒数"""
    start = sub.start.ordinal / 1000
    end = sub.end.ordinal / 1000
    return start, end

def add_subtitles(video_path, subtitles_path, output_path, font='STSong', fontsize=24, color='yellow', stroke_color='black', stroke_width=1):
    with VideoFileClip(video_path).subclip(0, 100) as video:
        subtitles = pysrt.open(subtitles_path, encoding='utf-8')
        clips = [video]  # 包含原始视频的列表

        try:
            for sub in subtitles:
                start, end = sub_to_seconds(sub)
                if start < 100:
                    end = min(end, 100)  # 调整字幕时间，确保它们在视频的前100秒内
                    txt_clip = TextClip(txt=sub.text, font=font, fontsize=fontsize, color=color, stroke_color=stroke_color, stroke_width=stroke_width)
                    txt_clip = txt_clip.set_duration(end - start).set_position(('center', 'bottom')).set_start(start)
                    clips.append(txt_clip)  # 将字幕剪辑添加到列表中

            # 使用原始视频的音频合成最终剪辑
            final_clip = CompositeVideoClip(clips)
            final_clip.audio = video.audio
            final_clip.write_videofile(output_path, codec='libx264', audio_codec='aac')
        except Exception as e:
            print(f"Error processing video: {e}")

if __name__ == '__main__':
    video_path = 'ASurvey.webm'
    subtitles_path = 'ASurvey.srt'
    output_path = 'output.mp4'
    add_subtitles(video_path, subtitles_path, output_path)
