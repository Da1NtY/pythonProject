import string
import random

char_set = string.printable.strip()

# 随机生成n个数，默认生成8位
def password_generator(n = 8):
    password = ""
    for i in range(1,n+1):
        char = random.choice(char_set)
        password += char
    return password

print(password_generator())