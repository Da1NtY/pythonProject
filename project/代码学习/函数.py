# 函数
'''
global: 在函数内部引入全局东西
nonlocal: 在局部引入外层的局部对象
'''
def func(*args):
    print(args)

stu_list = ["1","2","3"]
func(*stu_list) # *在实参位置，是把列表打散成位置参数进行传递
                # ** 在实参位置，可以把字典转换成关键字参数进行传递

# 要想在函数内部修改全局变量  关键字 global
a = 10
def func2():
    global a
    a = 20

func2()
print(a)

# nonlocal
def func3():
    a = 111
    def func2():
        nonlocal a
        a = 123
    func2()
    print(a)

func3()

