# 输入当前年、月、日
year = int(input('输入当前年：'))
month = int(input('输入当前月：'))
day = int(input('输入当前日：'))

# 输出 连字符’-‘分隔，如2024-3-1
print(year,month,day,sep='-')

# 输出 用字符串拼接方法输出，格式如 2024年3月1日
print(str(year) + '年' + str(month) + '月' + str(day) + '日')

# 输出 用str.format()格式输出，格式如 2024年3月1日
print("{}年{}月{}日".format(year,month,day))

# 输出 用f-string格式输出，格式如 2024年3月1日
print(f'{year}年{month}月{day}日')