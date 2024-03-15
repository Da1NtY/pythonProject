# 通过编写程序来获取到互联网上的资源

from urllib.request import urlopen

url = "http://www.baidu.com"
resp = urlopen(url)

with open("baidu.html", mode="w") as f:
    f.write(resp.read().decode("utf-8"))
print("over")