# 导入正则模块库
import re


# 定义一个类
class CounterWord:
    # 初始化
    def __init__(self, file_name):
        # 设置要统计单词的文件名
        self.filename = file_name
        # 初始化一个字典，用来保存各单词出现的次数
        self.dict_count = ()

    # 定义一个统计函数
    def count_word(self):
        # 以读取的方式打开文本文件
        with open(self.filename, 'r') as f:
            # 循环读取文件的每一行，防止应文件过大而造成卡顿
            for line in f:
                # 定义一个空的列表变量words，用于依次保存文件中每行的单词
                words = []
                # 用列表生成式把每行的各个单词加入进来
                words = [s.lower() for s in re.findall("\ w+", line)]

                # 通过循环统计单词的出现次数
                for word in words:
                    # 采用累加法计算单词的出现次数
                    # self.dict_count[word]是以单词命名的字典键
                    # self.dict_count.get(word, 0)表示如果字典中没有word代表的键，就返回0
                    # self.dict_count.get(word, 0) + 1表示每发现一次该单词就加1
                    self.dict_count[word] = self.dict_count.get(word, 0) + 1

    # 取出现次数在前num的单词
    def top_number(self, num):
        # 通过sorted()对字典进行排序，排序按键值大小排
        # 排序的方式是逆序的   reverse = True
        # 对排好序的字典进行切片，取前num个
        return sorted(self.dict_count.items(), key=lambda item: item[1], reverse=True)[:num]


# 主函数
if __name__ == '__main__':
    # 生成CounterWord实例对象
    counter_obj = CounterWord("test_count.txt")
    # 调用函数进行统计
    counter_obj.count_word()
    # 取出现次数最多的前六个单词
    top_num_6 = counter_obj.top_number(6)
    print("出现次数前6的单词统计如下")

    for word in top_num_6:
        print(word[0], '出现', word[1], '次')
