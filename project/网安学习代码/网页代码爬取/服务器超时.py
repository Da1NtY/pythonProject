import requests

url = "http://192.168.109.100/php/function/sleep.php"

try:
    res = requests.get(url,timeout= 10)
except:
    print("timeout!")

else:
    print(res.text)