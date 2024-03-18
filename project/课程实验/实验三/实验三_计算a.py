'''
编写程序，计算s=a+aa+aaa+aaaa+......+aaa...aaa(n个)，
其中a是1~9之间的某个数字，n是一个正整数。
如当a=2,n=5时，则s=2+22+222+2222+22222=24690。
【提示】如何表示该多项式中的某一项？
方法一：如果item表示当前项且为数值型，则下一项为item*10+a
方法二：利用字符串的乘法特性，如“2”*2的值为“22”，“2”*3的值为“222”。

试用以上两种方法分别编写程序，a和n的值由用户输入。

'''

# 用户输入a和n的值
a = int(input("请数入a的值："))
n = int(input("请输入n的值："))

# 方法一
# sum = a
# item = a
# for i in range(n-1):
#     item = item*10+a
#     sum = sum+item
#
# print(f"计算结果为：{sum}")

# 方法二

sum = 0
for i in range(1,n+1):
    str1 = str(a) * i
    sum = sum+int(str1)

print(f"计算结果为：{sum}")
