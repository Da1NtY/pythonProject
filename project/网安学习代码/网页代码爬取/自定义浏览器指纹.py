import requests

url = "http://192.168.109.100/php/functions/get.php"

headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/112.0)"
}

res = requests.get(url=url, headers=headers)

print(res.request.headers)