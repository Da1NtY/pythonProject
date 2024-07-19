import requests
import re
from bs4 import BeautifulSoup
import lxml
url = "http://192.168.109.100/pythonSpider/index.html"
res = requests.get(url= url,timeout=3)

# 响应对象中的属性
text = res.text
content = res.content
status_code = res.status_code
url1 = res.url
headers = res.headers
req_headers = res.request.headers
cookies = res.cookies

print(re.findall(r"style/\w*.jpg", text))
soup = BeautifulSoup(content, "lxml")
print(type(soup))
print(soup.find_all("img"))

