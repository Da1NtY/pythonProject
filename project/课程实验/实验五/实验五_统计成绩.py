'''
设计统计指定等级对应成绩人数的函数myCount(lst,grade=5),lst为成绩列表，grade为1～5的整数，对应5个等级（不及格、及格、中、良、优秀）。

若已知数据a=[45，67，78，89，90，66，88，99，77，75，86，80，91，92，94，100]，主调函数分别使用不同参数传递方式加以调用。
按位置参数调用: myCount(a,1),假设统计不及格的人数，grade为1
按默认值参数调用: myCount(a),取默认值为5,统计优秀的人数
按关键字参数调用: myCount(grade=2,b=a),统计及格的人数
'''
def myCount(lst,grade=5):
    count = 0
    if grade==1:
        for i in lst:
            if i < 60:
                count = count + 1
        print(f"不及格的人数为{count}")
    elif grade==2:
        for i in lst:
            if 60 <= i < 70:
                count = count + 1
        print(f"及格的人数为{count}")
    elif grade==3:
        for i in lst:
            if 70 <= i < 80:
                count = count + 1
        print(f"中的人数为{count}")
    elif grade==4:
        for i in lst:
            if 80 <= i < 90:
                count = count + 1
        print(f"良的人数为{count}")
    elif grade==5:
        for i in lst:
            if 90 <= i <= 100:
                count = count + 1
        print(f"优秀的人数为{count}")
    else:
        print("输入的成绩有问题！")
a= [45,67,78,89,90,66,88,99,77,75,86,80,91,92,94,100]
myCount(a,1)
myCount(a)
myCount(grade=2,lst=a)