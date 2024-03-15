'''
推导式：
    简化代码
    语法：
        列表推导式；[数据 for循环 if条件判断]
        集合推导式：{数据 for循环 if条件判断}
        字典推导式：{k:v for循环 if条件判断}

'''
lst = [i for i in range(10)]
print(lst)

# 创建一个列表[1、3、5、7、9]
lst = [i for i in range(10) if i % 2 == 1]
print(lst)

# 将下列的列表修改成字典
lst = ['赵本山','潘长江','奥特曼']

dict = {i:lst[i] for i in range(len(lst))}
print(dict)