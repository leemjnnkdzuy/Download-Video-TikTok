from api import API

import requests
import os

def get_video(link):
    data = API(link)

    if data:
        video = data.get('video')
        music = data.get('music')
        cover = data.get('cover')
        WatermarkedVideo = data.get('OriginalWatermarkedVideo')
        description = data.get('description')
        videoid = data.get('videoid')
        author = data.get('author')

        sanitized_video = str(video).replace("[", "").replace("]", "").replace("'", "")
        sanitized_music = str(music).replace("[", "").replace("]", "").replace("'", "")
        sanitized_cover = str(cover).replace("[", "").replace("]", "").replace("'", "")
        sanitized_WatermarkedVideo = str(WatermarkedVideo).replace("[", "").replace("]", "").replace("'", "")
        sanitized_description = str(description).replace("[", "").replace("]", "").replace("'", "")
        sanitized_video_id = str(videoid).replace("[", "").replace("]", "").replace("'", "")
        sanitized_author = str(author).replace("[", "").replace("]", "").replace("'", "")

        if not os.path.exists(sanitized_author):
            os.mkdir(sanitized_author)

        if not os.path.exists(f"{sanitized_author}/info"):
            os.mkdir(f"{sanitized_author}/info")

        with open(f"{sanitized_author}/info/{sanitized_video_id}.txt", 'w', encoding='utf-8') as file:
            file.write(f"Video: {sanitized_video}\n")
            file.write(f"Music: {sanitized_music}\n")
            file.write(f"Cover: {sanitized_cover}\n")
            file.write(f"WatermarkedVideo: {sanitized_WatermarkedVideo}\n")
            file.write(f"Description: {sanitized_description}\n")
            file.write(f"Video ID: {sanitized_video_id}\n")
            file.write(f"Author: {sanitized_author}\n")

        print(f"\nThông tin {sanitized_video_id} đã được tải xuống và lưu trong thư mục {sanitized_author}/info/")


        video_response = requests.get(sanitized_video)

        if video_response.status_code == 200:
            if not os.path.exists(f"{sanitized_author}/video"):
                os.mkdir(f"{sanitized_author}/video")
            
            with open(f"{sanitized_author}/video/{sanitized_video_id}.mp4", 'wb') as file:
                file.write(video_response.content)
            
            print(f"Video {sanitized_video_id} đã được tải xuống và lưu trong thư mục {sanitized_author}/video/")
        else:
            print("Không thể tải xuống video")


def clean_up(file):
    with open(file, 'w', encoding='utf-8') as f:
            f.write('')

def open_txt_file(file):
    file_path = file
    os.system(f'notepad.exe {file_path}')

def check_api_key():

    if not os.path.exists('api_key.txt'):
        print("Không thể mở file")

        if not os.path.exists('api_key.txt'):
            open('api_key.txt', 'w')
            if not os.path.exists('api_key.txt'):
                print("Không thể tạo file 'api_key.txt'")
                exit()
            else:
                print("File 'api_key.txt' đã được tạo")
    else:
            print("File đã được mở")


def check_api_key_empty(file):
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    if content == '':
        print("File 'api_key.txt' rỗng, hãy nhập API Key vào file 'api_key.txt'")
        open_txt_file('api_key.txt')
        if not os.path.exists('api_key.txt'):
            print("Không thể mở file 'api_key.txt'")
            check_api_key()
        else:
            print("File 'api_key.txt' đã được mở")

def import_array_from_file(file):
    with open(file, 'r', encoding='utf-8') as f:
        arr = f.readlines()
    return arr