# 定义函数
def fab(n):
    # 判断n的有效性
    if n<=0:
        return '传递的参数必须是大于0的正整数！'
    # 当 n 为1时，返回斐波那契数的第1个数 0
    elif n==1:
        return 0
    else:
        # 给前两个数赋值为 0 1
        a, b = 0, 1
        # 初始化一个列表变量，列表前两个值分别为 0 和 1
        fab_list = [0, 1]
        # 由于fab_list初始化时已经有两个数值，所以得到n个数只需循环n-2次即可
        for i in range(n-2):
            a, b =b, a+b
            # 把前两个数的和加入到列表中
            fab_list.append(b)
        # 返回列表
        return fab_list

n = int(input("请输入需要打印的斐波那契个数："))
print(fab(n))