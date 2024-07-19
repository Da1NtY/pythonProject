import re

s = "I say food not Good"

# 正则re匹配（['food']）,加r代表其是一个正则表达式
print(re.findall(r"[a-z]ood", s))
# ['food', 'Good'](.代表占一个字符, o{1,2}代表o出现一次或两次)
print(re.findall(r"[0-9a-zA-Z]ood", s))
print(re.findall(r".ood", s))
print(re.findall(r".o{1,2}.", s))

s1 = "How old are you? I'm 24"
# 匹配年龄
print(re.findall(r"[0-9][0-9]", s1))
print(re.findall(r"[0-9]{1,3}", s1))
print(re.findall(r"\d{1,3}", s1))

# 匹配字符(不包括符号)
print(re.findall(r"\w", s1))

# 匹配到无数次
print(re.findall(r"o+", s1))