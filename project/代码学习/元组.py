# tuple 元组 不可变的列表 地址不可变
t = ("张飞","哈哈哈","李白")
print(t)
print(t[1:3])

#1.若元组只有一个元素，要在元素后面加个逗号才是元组，否则为字符串
t = ("哈哈",)
print(type(t))

# 关于元组不可变（坑）
t = (1,2,3,["哈哈哈","哈1"])
t[3].append("好的")
print(t)