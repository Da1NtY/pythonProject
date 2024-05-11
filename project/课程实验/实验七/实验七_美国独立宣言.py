'''
已知字符串变量
sentence=” When in the Course of human events, it becomes necessary for one people to dissolve the political bands which have connected them with another, and to assume among the Powers of the earth, the separate and equal station to which the Laws of Nature and of Nature's God entitle them, a decent respect to the opinions of mankind requires that they should declare the causes which impel them to the separation.”
存放了美国独立宣言中的一段话。试编写程序，实现以下功能：
1）定义一个函数countWord(s)，统计字符串中各单词出现的次数，并将结果存入字典中并返回。
2）调用countWord(s)函数，统计sentence字符串中每个单词出现的次数，并输出统计结果
3）输出出现次数排在前5名的单词

【提示】
1）在统计之前需要对文本进行预处理，如去除标点符号、统一大小写等
2）可以通过字符串的split()方法对文本中的单词进行提取，生成一个列表
3）遍历列表，对列表中的元素进行统计。统计结果存放在字典中，键表示单词，值表示次数
'''
import re
from collections import Counter

sentence="When in the Course of human events, it becomes necessary for one people to dissolve the political bands which have connected them with another, and to assume among the Powers of the earth, the separate and equal station to which the Laws of Nature and of Nature's God entitle them, a decent respect to the opinions of mankind requires that they should declare the causes which impel them to the separation."

def countWord(s):
    # 去除标点符号
    s = re.sub(r'[^\w\s]', '', s)
    # 转换为小写
    s = s.lower()
    # 拆分成单词列表
    word_list = s.split()
    # 统计单词出现次数
    word_count = dict(Counter(word_list))
    return word_count

word_counts = countWord(sentence)

# 输出统计结果
print("单词出现次数统计结果:")
for word, count in word_counts.items():
    print(f"{word}: {count}")

# 获取出现次数排在前5名的单词
top_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)[:5]
print("\n出现次数排在前5名的单词:")
for word, count in top_words:
    print(f"{word}: {count}")