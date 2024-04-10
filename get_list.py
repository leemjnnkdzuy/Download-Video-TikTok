import re
import requests

def format():
    with open('input.txt', 'r', encoding='utf-8') as f:
        content = f.read()

    urls = re.findall(r'https://www\.tiktok\.com/@[^/]+/video/\d+', content)

    accessible_urls = []
    for url in urls:
        try:
            response = requests.head(url)
            if response.status_code == 200 and 'tiktok.com' in response.url:
                accessible_urls.append(url)
        except requests.exceptions.RequestException as e:
            print(f"Link không tồn tại {url}: {e}")

    with open('list.txt', 'w') as f:
        for url in accessible_urls:
            f.write(url + '\n')

def remove_duplicates():
    with open('list.txt', 'r') as f:
        urls = set(line.strip() for line in f)

    with open('list.txt', 'w') as f:
        for url in urls:
            f.write(url + '\n')

def print_list():
    with open('list.txt', 'r') as f:
        content = f.read()

    print(content)

def get_list():
    format()
    remove_duplicates()