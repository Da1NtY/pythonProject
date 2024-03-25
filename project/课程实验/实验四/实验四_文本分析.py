'''
文本分析。入一个字符串
1）统计字符串中大写字母、小写字母、数字、空格和其他字符的数量。
提示：
使用ch.isupper()方法判断字符是否为大写字母，返回True/False;
使用ch.islower()方法判断字符是否为小写字母，返回True/False;
使用ch.isdigit()方法判断字符是否为数字，返回True/False;
使用ch.isspace()方法判断字符是否为空白字符，包括空格、制表符、换行符、回车符、垂直制表符等，返回True/False;
判断空格可用是否为空格字符串‘ ’
2）统计字符串中单词的数量
提示：将字符串中的符号替换为空格，再用split()方法以空格为分隔符，返回单词的列表再用len()函数获取列表的长度，即单词的数量
3）提取每个单词的首字母，拼接为一个字符串
提示：用循环遍历上题获得的单词列表，取出每个单词的首字母，拼接为一个字符串
4）用凯撒加密方法对字符串进行加密
为提高加密强度，约定输入一个秘密单词来产生偏移量。
偏移量计算方法为：
字母字符----计算用户输入的秘密单词中每个字符的Unicode值的和，再对26取模，为避免偏移量恰好为0，本题约定秘密单词为用于表示星期几的单词，即
'Monday'、'Tuesday'、'Wednesday'、'Thursday'、'Friday'、'Saturday'、'Sunday'
数字字符----用秘密单词的长度对10取模.

测试用例：
输入:：
请输入一个待加密的句子：Attack on Pearl Harbor on December 7,1941
输出：
大写字母:4,小写字母:25,数字:5,空格:6,其他:1
句子的单词数是:7
各单词的首字母是：AoPHoD7
继续输入：
请输入一个秘密单词:Monday
输出：
Sllsuc gf Hwsjd Zsjtgj gf Vwuwetwj 3,7507

'''

# 用户输入
s = str(input("请输入一个待加密的句子:"))

# 统计字符串中大写字母、小写字母、数字、空格和其他字符的数量
num_up = 0
num_low = 0
num_nu = 0
num_sp = 0
num_ot = 0
for i in s:
    if i.isupper():
        num_up += 1

    elif i.islower():
        num_low += 1

    elif i.isdigit():
        num_nu += 1

    elif i.isspace():
        num_sp += 1

    else:
        num_ot += 1

print(f"大写字母:{num_up},小写字母:{num_low},数字:{num_nu},空格:{num_sp},其他:{num_ot}")

# 统计字符串中单词的数量
words = s.split()

word_count = len(words)

print(f"句子的单词数是:{word_count}")

# 提取每个单词的首字母，拼接为一个字符串
str_sum = ""
for item in words:
    Item = item[0:1]
    str_sum += Item

print(str_sum)

# 用凯撒加密方法对字符串进行加密
# 为提高加密强度，约定输入一个秘密单词来产生偏移量。

# 用户输入秘密单词
word_secret = str(input("请输入一个秘密单词:"))

def caesar_encrypt(str_need, secret_word):
    # 计算字母偏移量
    letter_offset = sum(ord(char) for char in secret_word) % 26
    # 计算数字偏移量
    digit_offset = len(secret_word) % 10
    # 字符串加密函数
    def shift_char(char):
        if char.isalpha():
            base = ord('a')if char.islower() else ord('A')
            return chr((ord(char)-base+letter_offset) % 26 + base)
        elif char.isdigit():
            return chr((ord(char)-ord('0')+digit_offset) % 10 + ord('0'))
        else:
            return char
    # 加密字符串
    text1 = ''.join(shift_char(char) for char in str_need)

    return text1

text_secret = caesar_encrypt(s, word_secret)

print(text_secret)