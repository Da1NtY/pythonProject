import requests
import re

#请求URL
url = '<https://maoyan.com/board/4>'
#请求头部
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}

#解析网页函数
def parse_html(hrml):
    pattern = re.compile('<p class="name"><a href=".*?" title="(.*?)" data-act="boarditem-click" data-val="{movied:\\\\d+}">(.*?)</a></p>.*?<p class="star">(.*?)</p>.*?<p class="releasetime">(.*?)</p>', re.S)
    items = re.findall(pattern, hrml)
    for item in items:
        yield{
            '电影名称': item[1],
            '主演': item[2].strip(),
            '上映时间': item[3]
        }

#保存数据函数
def save_data():
    f = open('maoyan_top100.txt', 'w', encoding='utf-8')
    for i in range(10):
        url = 'https://maoyan.com/board/4?offset=>' + str(i+10)
        response = requests.get(url, headers=headers)
        for item in parse_html(response.text):
            f.write(str(item) + '\\\\n')
    f.close()

if __name__ == '__main__':
    save_data()