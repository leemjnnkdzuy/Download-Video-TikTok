from api import API
from get_list import get_list, print_list
from file_process import json_to_excel
from check_err import check_list_empty

import requests
import os
import re

def get_video(link):
    data = API(link)

    user_name = re.findall(r'https://www\.tiktok\.com/@([^/]+)/video/\d+', link)[0]

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
        sanitized_videoid = str(videoid).replace("[", "").replace("]", "").replace("'", "")
        sanitized_author = str(author).replace("[", "").replace("]", "").replace("'", "")

        if not os.path.exists(user_name):
            os.mkdir(user_name)

        if not os.path.exists(f"{user_name}/info"):
            os.mkdir(f"{user_name}/info")

        with open(f"{user_name}/info/{sanitized_videoid}.txt", 'a', encoding='utf-8') as file:
            file.write(f"Video: {sanitized_video}\n")
            file.write(f"Music: {sanitized_music}\n")
            file.write(f"Cover: {sanitized_cover}\n")
            file.write(f"WatermarkedVideo: {sanitized_WatermarkedVideo}\n")
            file.write(f"Description: {sanitized_description}\n")
            file.write(f"Video ID: {sanitized_videoid}\n")
            file.write(f"Author: {sanitized_author}\n")

        print(f"\nThông tin {sanitized_videoid} đã được tải xuống và lưu trong thư mục {user_name}/info/")

        if not os.path.exists(f"{user_name}/excel"):
            os.mkdir(f"{user_name}/excel")

        with open(f"{user_name}/excel/{user_name}.json", 'a', encoding='utf-8') as file:
            file.write(f"{data}\n")

        video_response = requests.get(sanitized_video, timeout=20)

        if video_response.status_code == 200:
            if not os.path.exists(f"{user_name}/video"):
                os.mkdir(f"{user_name}/video")
            
            with open(f"{user_name}/video/{sanitized_videoid}.mp4", 'wb') as file:
                file.write(video_response.content)
            
            print(f"Video {sanitized_videoid} đã được tải xuống và lưu trong thư mục {user_name}/video/")
        else:
            print("Không thể tải xuống video")

def start():

    print("Đang tải danh sách video...")

    get_list()

    print("Đã tải xong danh sách video!")
    print("Đây là danh sách video: ")
    print_list()

    with open('list.txt', 'r', encoding='utf-8') as file:
        content = file.read()

    check_list_empty('list.txt')

    urls = re.findall(r'https://www\.tiktok\.com/@[^/]+/video/\d+', content)
    #user_name = re.findall(r'https://www\.tiktok\.com/@([^/]+)/video/\d+', content)[0]

    total = len(urls)
    for i, url in enumerate(urls):
        get_video(url)
        print(f"Đã tải: {i+1} / {total}")

    #json_to_excel(f'{user_name}/excel/{user_name}.json', f'{user_name}/excel/data.xlsx')

    #delete_file(f'{user_name}/excel/{user_name}.json')

    print("Tải xuống hoàn tất!")