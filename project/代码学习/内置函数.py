# 内置函数：直接拿来用的函数
'''
sorted: 排序

filter: 筛选

map: 批量处理
'''
# bin,oct,hex
a = 18
print(bin(a))  # 0b10010 二进制
print(oct(a))  # 0o22    八进制
print(hex(a))  # 0x12    十六进制

# format 格式化
print(format(a,"b")) # b:二进制 o:八进制 x:十六进制
print(format(a,"08b")) # 表示得到一个8位的二进制数

lst = list("呵呵哒")
print(lst)

# enumerate,all,any
print(all([1,"11","111"])) # 相当于and
print(any([1,1])) # 相当于or

lst = ["啧啧啧","哈哈哈","啦啦啦"]

for index,item in enumerate(lst):
    print(index,item)

# hash 哈希
s = "呵呵哒"
print(hash(s)) # 一定是一个数字 -> 想办法转化成内存地址，然后进行数据的存储 -> 字典（集合）哈希表

# help

# zip   把多个可迭代内容进行合并
lst1 =["赵本山","范伟","苏有朋"]
lst2 =[40,38,42]
lst3 = ["卖拐","耳朵大有福","情深深雨蒙蒙"]

result = zip(lst1,lst2,lst3)
for item in result:
    print(item)

# locals 当前作用域里的内容

# globals  全局作用域里的内容

# sorted
lst1 = [1,2,3,4,5,6,7,8]
s = sorted(lst1, reverse=True)
print(s)

lst1 = ["八嘎亚路", "哒唛吆", "吆西", "哈撒ki"]

s = sorted(lst1, key= lambda x:len(x), reverse=True)
print(s)

# filter
lst = ["八嘎亚路", "哒唛吆", "吆西", "哈撒ki"]
f = filter( lambda x: x.startswith("哒"), lst)
print(list(f))

# map
lst = [1,2,3,4,5,6,7,8]
r = map( lambda x: x*x ,lst)
print(list(r))