from func import get_video, clean_up, open_txt_file
from get_list import get_list, print_list
from welcome import welcome
from func import check_api_key, check_api_key_empty

import re
import os

def start():
    print("Đang tải danh sách video...")

    get_list()

    print("Đã tải xong danh sách video!")
    print("Đây là danh sách video: ")
    print_list()

    with open('list.txt', 'r', encoding='utf-8') as f:
        content = f.read()

    urls = re.findall(r'https://www\.tiktok\.com/@[^/]+/video/\d+', content)

    total = len(urls)
    for i, url in enumerate(urls):
        get_video(url)
        print(f"Đã tải: {i+1} / {total}")

    os.remove('list.txt')

    print("Tải xuống hoàn tất!")

while __name__ == "__main__":

    welcome()

    check_api_key()
    check_api_key_empty('api_key.txt')


    if not os.path.exists('input.txt'):
        print("File 'input.txt' không tồn tại")
        open('input.txt', 'w')
        if not os.path.exists('input.txt'):
            print("Không thể tạo file 'input.txt'")
            exit()
        else:
            print("File 'input.txt' đã được tự động tạo!")

    with open('input.txt', 'r', encoding='utf-8') as f:
        content = f.read()

    

    if content == '':
        print("File 'input.txt' rỗng, hãy import Source Code của trang tiktok vào file 'input.txt'")
        open_txt_file('input.txt')
        if not os.path.exists('input.txt'):
            print("Không thể mở file 'input.txt'")
            exit()
        else:
            print("File 'input.txt' đã được mở")
    else:
        start()

        print("\n\nBạn có muốn tiếp tục tải xuống không?")
        print("1. Có")
        print("2. Không")
        choice = input("Chọn: ")
        if choice == '1':
            clean_up('input.txt')
            print("File 'input.txt' đã được làm sạch!")
            open_txt_file('input.txt')
            start()
        else:  
            print("Kết thúc chương trình")
            exit()