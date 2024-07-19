import requests

# 获取网页HTML源代码
url = "http://192.168.109.100/pythonSpider/index.html"

def get_html(url):
    res = requests.get(url)
    return res.content

print(get_html(url))
