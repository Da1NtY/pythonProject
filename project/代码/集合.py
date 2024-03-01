# set集合
# 可以用来去除重复
# 无索引无切片
s = {1,2,3}
print(type(s))
print(s) # 无序的

# python中的set集合进行数据存储时，需要对数据进行哈希计算，根据计算出来的哈希值进行存储数据
# 可哈希：不可变的数据类型：int str tuple bool
# 不可哈希：可变的数据类型：list dict set

s = set() #创建空集合
s.add("哈哈哈")
s.add("呵呵")
print(s)

s.remove("呵呵")
print(s)

#若要修改，需要先删除再新增

# 交集，并集，差集
s1 = {1,2,3,4}
s2 = {3,4,5,6}

print(s1 & s2) #交集
print(s1.intersection(s2))
print(s1 | s2) #并集
print(s1.union(s2))
print(s1 - s2) #差集
print(s1.difference(s2))