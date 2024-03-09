import re

# 定义一个函数，通过该函数查找文本字符串的每一个单词
# 然后计算每个单词出现的次数，最后按照出现次数从多到少放到列表变量中
def get_char(txt):
    # 通过re.split()函数将英文单词分别取出来，函数的第一个参数为分隔符
    # 第一个参数指定以":" ";" "," "." "“" 和空格（\s）以及多个空格（\s*）作为分隔符
    # 第二个参数是要拆分的字符串
    # 将分割出来的单词放到列表valist中
    vlist = re.split('[:;,."\s]\s*',txt)

    # 生产字典变量
    vdic_frequency = dict()

    # 遍历列表变量vlist
    for vchar in vlist:
        # 取出每个单词，并判断字典中是否存在一个元素项（键值对）
        if vchar in vdic_frequency:
            # 如果存在，将以单词命名的键的值加1
            vdic_frequency[vchar] += 1
        else:
            # 如果不存在，增加一个单词命名的键，并设置其键值为1
            vdic_frequency[vchar] = 1
    # 对字典中的项按键值进行排序，并且是倒序排序（reverse = True）
    vdic_sort = sorted(vdic_frequency.items(), key = lambda item : item[1], reverse=True)
    return vdic_sort

# 主函数
if __name__ == '__main__':
    # 打开文件，读出文件的文本
    # 其中test.txt文件是当前目录下的一篇英文文章，文本类型
    with open('test.txt', 'r') as f:
        vtext = f.read()
    #调用排序函数
    vstr = get_char(vtext)
    print('列出文本中的英文单词：\n')

    # 在终端上打印文本中的单词
    print(vstr)