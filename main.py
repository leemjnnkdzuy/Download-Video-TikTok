
from welcome import welcome
from file_process import open_txt_file, clean_up, real_file, delete_file
from check_err import check_file_exist, check_empty
from main_func import start
from video_func import mirror_videos

while __name__ == "__main__":

    welcome()

    check_file_exist('api_key.txt')
    check_empty('api_key.txt')

    check_file_exist('input.txt')

    content = real_file('input.txt')
    
    if content == '':
        check_empty('input.txt')
    else:
        start()

        print("\n\nBạn có muốn chỉnh sửa toàn bộ video sơ bộ không?")
        print("1. Có")
        print("2. Không")
        choice = input("Chọn: ")
        if choice == '1':
            mirror_videos()
            print("\n\nChỉnh sửa toàn bộ video sơ bộ đã hoàn tất!")
        else:
            print("Toàn bộ video được giữ nguyên!")

        delete_file('list.txt')

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