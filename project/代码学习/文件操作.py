'''
文件路径：
1。绝对路径
    C：/。。。
2.相对路径（用的更多）
    。/user/111.doc

../  表示上一层文件夹
mode:
    r: read 读取
    w: write 写入
    a: append 追加写入
    b: 读写的是非文本文件

with:
    上下文，不需要手动去关闭一个文件
'''
import os

f = open("./文件案例/测试.txt",mode="r",encoding="utf-8")

# content = f.read() # 全部读取
# print(content)
#
# line = f.readline().strip() # 去掉字符串左右两端的空白，空格，换行，制表符。
# print(line)
#
# line = f.readline().strip()
# print(line)
#
# line = f.readline().strip()
# print(line)
#
# line = f.readlines()
# print(line)


# 最重要的文本读取方式
for line in f:  # 从f中读取每行数据
    print(line.strip())


# 写入文件
# w模式下，如果文件不存在，自动创建一个文件
# w模式下，每一次open都会清空掉文件中的内容
# f = open("./文件案例/测试1.txt",mode="w",encoding="utf-8")
# f.write("大大大")
#
# f.close()  # 要关闭链接


# 追加写入文件
f = open("./文件案例/测试1.txt",mode="a",encoding="utf-8")
f.write("666")

# with
with open("./文件案例/测试1.txt",mode="r",encoding="utf-8") as f:
    for line in f:
        print(line.strip())

# 读取图片
# with open("./文件案例/图片.dng",mode="rb") as f:
#     for line in f:
#         print(line)

# 文件的复制
# 从原文件中读取文件，写入到新路径中
# with open("./文件案例/图片.dng",mode="rb") as f1,\
#     open("./文件案例/复制/图片.dng",mode="wb") as f2:
#     for line in f1:
#         f2.write(line)

# 文件的修改
# 把文件中的周 ——》张
with open("./文件案例/人名单.txt",mode="r",encoding="utf-8") as f1, \
    open("./文件案例/人名单_副本.txt",mode="w",encoding="utf-8") as f2:
    for line in f1:
        line = line.strip() # 去掉换行
        if line.startswith("周"):
            line = line.replace("周","张")

        f2.write(line)
        f2.write("\n")

# 删除原文件
os.remove("./文件案例/人名单.txt")
# 把副本文件重命名
os.rename("./文件案例/人名单_副本.txt", "./文件案例/人名单.txt")