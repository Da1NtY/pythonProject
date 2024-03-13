'''
输入年份和月份，输出该月份的天数
让用户分别输入年份和月份，然后程序输出该年份和该月份的天数。
要考虑到闰年（闰年的2月份有29天，平年的2月份有28天）。
分别测试2019年的2月，5月，10月以及2020年的2月，6月，11月
'''

# 用户输入年份和月份
year = int(input('请输入年份：'))
month = int(input('请输入月份：'))

if year % 4 == 0 and year % 100 != 0:
    if month == 2:
        days =29
    elif month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        days = 31
    else:
        days = 30
else:
    if month == 2:
        days = 28
    elif month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        days = 31
    else:
        days = 30

# 输出
print("该月有{}天".format(days))