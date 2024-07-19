import requests
import re
import time

# 获取网页HTML源代码
url = "http://192.168.109.100/pythonSpider/index.html"

def get_html(url):
    res = requests.get(url = url)
    return res.text

# 获取图片地址
def  get_img_path_list(html):
    img_path_list = re.findall(r"style/\w*.jpg", html)
    return img_path_list

# 下载图片
def download_img(url,img_path_list):
    for img_path in img_path_list:
        img_url = url[0:url.rfind("/") + 1] + img_path
        res = requests.get(url = img_url)
        img_save_path = f"./images/{time.time()}.jpg"

        with open(img_save_path, 'wb') as f:
            f.write(res.content)

html = get_html(url)
img_path_list = get_img_path_list(html)
download_img(url,img_path_list)