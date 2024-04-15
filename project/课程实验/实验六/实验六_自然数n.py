'''
让用户在键盘上输入一个自然数n，然后在区间[1,5n]上随机生成n个不重复的自然数，输出这些自然数；
然后继续编写代码，分别用filter()函数和列表生成式对这些自然数进行处理，只保留所有偶数，并输出这些偶数。
【提示】：可先生成[1,5n]内的所有整数，然后用random.sample()函数从中随机选出n个数。
'''
import random

# 用户输入自然数n
n = int(input("请输入一个自然数n："))

# 生成[1,5n]内的所有整数列表
all_nums = list(range(1, 5*n+1))

# 从all_nums中随机选出n个数
random_nums = random.sample(all_nums, n)
print("随机生成的自然数为：", random_nums)

# 使用filter()函数保留偶数
even_nums_filter = list(filter(lambda x: x % 2 == 0, random_nums))
print("使用filter()函数保留的偶数为：", even_nums_filter)

# 使用列表生成式保留偶数
even_nums_list_comp = [num for num in random_nums if num % 2 == 0]
print("使用列表生成式保留的偶数为：", even_nums_list_comp)