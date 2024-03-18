'''
九章算术》中有一个有趣的问题：今有垣厚十尺，两鼠对穿。大鼠日一尺，小鼠亦一尺。
大鼠日自倍，小鼠日自半。问何日相逢？
要求使用循环完成，不允许使用幂运算。
测试用例：
输入格式：
输入一个数，代表墙的厚度，单位为尺：10
输出格式：
第4天两只老鼠相遇

'''

# 用户输入墙的厚度
len_wall = int(input("输入一个数，代表墙的厚度，单位为尺："))

big_mouse = 1
small_mouse = 1
len_work = 0

for i in range(1,len_wall+1):
    if i == 1:
        big_mouse = 1
        small_mouse = 1
    else:
        big_mouse *= 2
        small_mouse /= 2

    len_work = big_mouse + small_mouse +len_work
    if len_work >= len_wall:
        print(f"第{i}天两只老鼠相遇")
        break
