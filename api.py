import requests

def API(link):
    url = "https://tiktok-downloader-download-tiktok-videos-without-watermark.p.rapidapi.com/vid/index"

    querystring = {"url": link}

    headers = {
        "X-RapidAPI-Key": "9cf5a71810msh1694cf5276f68f3p15199cjsn34794d661141",
        "X-RapidAPI-Host": "tiktok-downloader-download-tiktok-videos-without-watermark.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    if response.status_code == 200:
        return response.json()
    else:
        print("Lỗi khi gửi yêu cầu API")
        return None