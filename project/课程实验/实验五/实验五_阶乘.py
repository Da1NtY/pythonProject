'''
编写求阶乘函数f(n)，调用f(n)计算组合数C62的值。
'''
def jiecheng(a,b):
    x = 1
    y = 1
    z = 1
    for i in range(1,a+1):
        x = i * x
    for i in range(1,b+1):
        y = i * y
    for i in range(1,a-b+1):
        z = i * z
    result = x / y / z
    return result
print("合数的值为{}".format(jiecheng(6,2)))