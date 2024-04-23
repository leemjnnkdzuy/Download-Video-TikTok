from file_process import open_txt_file, clean_up, open_txt_file, real_file

import os

def check_file_exist(file):
    if not os.path.exists(file):
        print("File " + file + " không tồn tại")

        if not os.path.exists(file):
            open(file, 'w')
            if not os.path.exists('api_key.txt'):
                print("Không thể tạo file " + file)
                exit()
            else:
                print("File " + file + " đã được tạo")

def check_empty(file):
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    if content == '':
        print("File " + file + " rỗng, hãy nhập API Key vào file " + file)
        if not os.path.exists(file):
            print("Không thể mở file " + file)
            check_file_exist(file)
        else:
            print("File " + file + " đã được mở")
            open_txt_file(file)

def check_list_empty(file):
    content = real_file(file)
    if content == '':
        print("File " + file + " rỗng, hãy nhập lại dữ liệu vào file input.txt")
        clean_up("input.txt")
        clean_up(file)
        open_txt_file("input.txt")
        