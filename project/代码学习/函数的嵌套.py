"""
函数可以嵌套函数

1. 函数可以作为返回值进行返回
2. 函数可以作为参数进行互相传递
"""
def func1():
    b = 1
    def func2(): # 局部的东西，一般都是自己调用进行访问
        pass

# 例子
def func():
    print(123)
    def func2():
        print(456)
        def func3():
            print(789)
        print(1)
        func3()
    func2()
    print(2)
print(3)

func()

# 返回函数 可以将函数内部的函数搞出来
def func11():
    def inner():
        print(123)
    return inner
b1 = func11()
b1()   # b1 是函数名   函数本身也是一个变量
