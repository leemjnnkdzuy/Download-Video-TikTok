import requests 

def read_api_key(file):
    with open(file, 'r', encoding='utf-8') as f:
        api_key = f.read()
    return api_key

def API(link):
    url = "https://tiktok-downloader-download-tiktok-videos-without-watermark.p.rapidapi.com/vid/index"
    
    api = read_api_key('api_key.txt')

    querystring = {"url": link}

    headers = {
        "X-RapidAPI-Key": api,
        "X-RapidAPI-Host": "tiktok-downloader-download-tiktok-videos-without-watermark.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    if response.status_code == 200:
        return response.json()
    else:
        print("Lỗi khi gửi yêu cầu API")
        return None