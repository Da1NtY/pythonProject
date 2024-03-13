'''
已知在同一个笼子中有鸡和兔共M只，鸡和兔的总脚数为N只，
求鸡和兔各有多少只。编程计算笼中各有多少只鸡和兔，假设鸡和兔都正常，无残疾。
如无解则输出‘Data Error’。
测试用例：
输入1：
请输入头数,脚数：11,46
输出1：
数据错误

输入2：
请输入头数,脚数：11,42
输出2：
鸡1只，兔子10只

输入3：
请输入头数,脚数：11,18
输出3：
数据错误

输入4：
请输入头数,脚数：22,45
输出4：
数据错误

'''

# 输入头数,脚数
head = int(input("请输入头数："))
feet = int(input("请输入脚数："))


for i in range(head):
    for j in range(head):
        if (i + j) == head and (2*i + 4*j) == feet:
            print("鸡{}只".format(str(i)))
            print("兔{}只".format(str(j)))
            break
        elif i == head and 2*i != feet:
            print("Data Error")
