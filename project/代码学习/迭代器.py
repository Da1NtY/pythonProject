'''
str list tuple dict set open()

可迭代的数据类型会提供一个迭代器，这个迭代器可以帮我们把数据类型中的所有数据逐一拿到

获取迭代器的两种方法：
            1.iter()  内置函数   可直接拿到迭代器
            2__iter__()  特殊方法

从迭代器中获取数据的方法：
            1.next()
            2.__next__()

for 里面一定是要拿迭代器的，所有所有不可迭代的东西不能用for循环
for 里面一定有next出现

迭代器本身也是可迭代的内容

特性：
    1.迭代器只能向下去拿，不能反复
    2.特别节省内存
    3.惰性机制

总结：
    迭代器统一了不同数据类型的遍历工作
'''

it = iter("你叫什么名字")
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))   # StopIteration 迭代停止了，不可以再次从迭代器中拿数据了

it = "呵呵哒".__iter__()
print(it.__next__())
print(it.__next__())
print(it.__next__())

# 模拟for循环工作原理

s = "我是数据"
it = iter(s)
while 1:
    try:
        data = next(it)
        print(data)
    except StopIteration as e:
        break


