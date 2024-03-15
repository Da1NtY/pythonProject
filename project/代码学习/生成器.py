'''
生成器（generator）的本质是迭代器

优势：
    节省内存

    创建生成器的两种方案：
        1.生成器函数
        2.生成器表达式

        生成器函数：
            生成器函数中有一个关键字yield

        yield:
            1.可以返回数据
            2.可以分段的执行函数中的内容，通过__next__()可以执行到下一个yield的位置

    生成器表达式：
        语法（数据 for if）
'''

# def func():
#     print(123)
#     yield 999
#     print(456)
#     yield 666
#
# ret = func()
# print(next(ret))
# print(next(ret))

# 工厂生产衣服
def order():
    lst = []
    for i in range(10000):
        lst.append(f"衣服{i}")
        if len(lst) == 50:
            yield lst
            # 下一次拿数据
            lst = []

ord = order()
print(next(ord))
print(next(ord))

# 生成器表达式
gen = (i**2 for i in range(10))
print(next(gen))
print(next(gen))

lst = list(gen)
print(lst)