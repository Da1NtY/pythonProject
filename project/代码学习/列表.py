#所有东西都能装到列表中
#1.可以用索引和切片
#2.索引超过范围会报错
#3.可以用for循环进行遍历
#4.用len可以拿到列表的长度
lst = [1,2,3,4,5,6,7,8,9]
print(lst[0])
print(lst[1:5])
print(lst[::-1])

#列表的增删改查
lst = []

#向列表中添加内容
#append()在列表最后进行追加
lst.append("武则天")
lst.append("孙悟空")
lst.append("李白")
#insert()插入
lst.insert(0,"嬴政")
#extend()合并两个列表
lst.extend(["程咬金","鲁班"])

#删除
#pop()给出被删除的索引，返回被删除的元素
ret = lst.pop(2)
print(lst)
print(ret)
#remove()删除元素
lst.remove("武则天")

#修改
lst[3] = "凯"
print(lst)

#查询
print(lst[3])

#练习
# 把所有姓张的人改成姓王
lst = ["张飞","嬴政","张益达"]

for i in range(len(lst)):
    if lst[i].startswith("张"):
        new_name = lst[i].replace("张","王")
        lst[i] = new_name
print(lst)

#列表排序
lst = [11,222,31,4212,522,61,722,82,9]
lst.sort() #对列表进行升序排序
lst.sort(reverse=True) #reverse 翻转 降序排序
print(lst)

#列表的嵌套
lst = [11,222,31,4212,[111,2,[211,22,12],522]]
print(lst[4][2][0])

#列表的循环删除
lst = ["张飞","嬴政","张益达","李白"]
temp = []
for item in lst:
    if item.startswith("张"):
        temp.append(item) #把要删除的东西记下来

for item in temp:
    lst.remove(item)
print(lst)