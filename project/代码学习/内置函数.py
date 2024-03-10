# 内置函数：直接拿来用的函数

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
