import os
from openai import OpenAI
os.environ["OPENAI_API_KEY"] = "sk-"

def checkGPT1(srtcontent):
    prompt="""
    将下面内容转化为中文，保持原有格式不变
    -----
    {}
    """.format(srtcontent)
    client = OpenAI()
    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a highly skilled translator with extensive experience in translating English content into Chinese, particularly in the context of technology and media. You possess a deep understanding of both languages, including technical jargon and cultural nuances, which enables you to provide accurate and contextually appropriate translations. You are adept at handling complex translations that require not only linguistic accuracy but also an understanding of the technical content and its implications. Your expertise allows you to translate subtitles from English to Chinese effectively, ensuring that the message conveyed is clear, precise, and maintains the integrity of the original content. Your work is crucial in bridging communication gaps and making information accessible to a broader audience."},
        {"role": "user", "content": prompt}
        ]
    )
    print(completion.choices[0].message.content)
    with open("ASurvey-cn.srt", "w") as file:
        file.write(completion.choices[0].message.content)

def checkGPT2(srtcontent):
    prompt="""
    归纳下面对话内容的核心观点，给出最合适的标题，并以checklist的格式，用中文提供核心金句清单
    -----
    {}
    """.format(srtcontent)
    client = OpenAI()
    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a skilled analyst with a deep understanding of discourse analysis. Your expertise enables you to distill complex dialogues into their core ideas, and you excel at summarizing and encapsulating key points in a concise and impactful manner. You can efficiently identify the central theme of a conversation and suggest an apt title and a core content phrase that captures the essence of the discussion. Your ability to analyze and interpret dialogue makes you adept at providing clear and insightful summaries that highlight the main arguments and perspectives presented. Your skills are invaluable for anyone seeking to grasp the fundamental aspects of a conversation quickly and accurately."},
        {"role": "user", "content": prompt}
        ]
    )
    print(completion.choices[0].message.content)

def read_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        print("文件未找到。")
        return None

def main():
    file_path = "ASurvey.srt"  # 请替换为你的文件路径
    mstr = read_file(file_path)
    checkGPT1(mstr)
    checkGPT2(mstr)
    

print("input your Youtube Address")
youtbAddr = input()
## https://www.youtube.com/watch?v=MnrJzXM7a6o
os.system("rm -rf ASurvey.*")
os.system("yt-dlp -f 'bestvideo[ext=webm]+bestaudio[ext=webm]/best[ext=webm]' -o 'ASurvey.%(ext)s' " + youtbAddr)
os.system("whisper ASurvey.webm --task translate --language Chinese --model small --output_format srt")
main()
