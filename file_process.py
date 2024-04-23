import os
import pandas as pd
import json

def real_file(file):
    return os.path.realpath(file)

def clean_up(file):
    with open(file, 'w', encoding='utf-8') as f:
            f.write('')

def open_txt_file(file):
    file_path = file
    os.system(f'notepad.exe {file_path}')

def import_array_from_file(file):
    with open(file, 'r', encoding='utf-8') as f:
        arr = f.readlines()
    return arr

def fix_json(json_file):
    with open(json_file, 'r') as f:
        content = f.read()
    fixed_content = content.replace("'", '"')
    with open(json_file, 'w') as f:
        f.write(fixed_content)

def json_to_excel(json_file, excel_file):
    fix_json(json_file)
    with open(json_file, 'r') as f:
        data = json.load(f)

    df = pd.DataFrame(data)
    df.to_excel(excel_file, index=False)

def delete_file(file):
    if os.path.exists(file):
        os.remove(file)
    else:
        print("File " + file + " không tồn tại")