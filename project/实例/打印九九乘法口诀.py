# for循环，其中range(1,10)取1~9之间的整数，不会取到10
for i in range(1,10):
    for j in range(1, i+1):
        # print()函数默认自带换行，可以添加第二个参数end = " " 来阻止换行并在每个式子后加一个空格
        print('{}*{}={}'.format(i, j, i*j),end=" ")
    # 换行
    print('')