#小数
print(10/3) #小数：数据范围是无限的. 整数：在某一个特定的区间内是可以表示的很清楚的

#在Python中，所有的非零的数字都是True，零是False
#在Python中，所有的非空字符串都是True，空字符串是False
while 1:
    content = input("请输入你要说的话：")
    if content:
        print("你说的话是",content)
    else:
        break
#字符串的格式化问题
# %s 字符串占位
# %d 占位整数
# %f 占位小数
name = input("请输入你的名字：")
address = input("请输入你的地址：")
age = int(input("请输入你的年龄："))
hobby = input("请输入你的爱好：")

s = "我叫%s，我住在%s，我今年%d岁，我喜欢做%s" % (name, address, age, hobby)
s1 = "我叫{}，我住在{}，我今年{}岁，我喜欢做{}".format(name, address, age, hobby)
#f-string
s2 = f"我叫{name}，我住在{address}，我今年{age}岁，我喜欢做{hobby}"
print(s)
print(s1)
print(s2)