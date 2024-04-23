from moviepy.editor import VideoFileClip, vfx
import os
import re

def video_mirror(filepath, output_dir):
    video = VideoFileClip(filepath)
    out = video.fx(vfx.mirror_x)
    filename = os.path.basename(filepath)
    out.write_videofile(os.path.join(output_dir, filename))

def get_video_files(directory):
    return [os.path.join(directory, f) for f in os.listdir(directory) if f.endswith(('.mp4'))]

def process_videos(input_dir, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    video_files = get_video_files(input_dir)
    for file in video_files:
        video_mirror(file, output_dir)

def mirror_videos():
    with open('list.txt', 'r', encoding='utf-8') as file:
        content = file.read()

    matches = re.findall(r'https://www\.tiktok\.com/@([^/]+)/video/\d+', content)

    if matches:
        user_name = matches[0]
        input_dir = f'{user_name}/video/'
        output_dir = f'{user_name}/video_output/'
        process_videos(input_dir, output_dir)
    else:
        print("Không tìm thấy user_name trong list.txt")