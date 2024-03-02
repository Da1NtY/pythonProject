# 字典是以键值对的形式存储数据的
# 字典的表示方式：{ket:value,key2:value}
dic = {"jay":"周杰伦","dad":"哈哈哈"}

val = dic["jay"]
print(val)

#字典的key必须是可哈希的数据类型
#字典的value可以是任意数据类型

#字典的增删改查
dic = dict()

# 增
dic['jay'] = "周杰伦"
dic['1'] = 123
dic.setdefault("2","321") # 设置默认值，如果已经有了key，则不起作用

# 修改
dic['jay'] = "ikun"
print(dic)

# 删除
dic.pop("jay")
print(dic)

# 查找
print(dic['1']) #如果key不存在，程序会报错
print(dic.get('1')) # 如果key不存在，程序会返回None

#None
a = None
print(type(a))

# 循环和嵌套
# 1.使用for循环，直接拿到key
for key in dic:
    print(key,dic[key])

# 2.把所有的key全部保存在一个列表中
print(list(dic.keys()))

# 3.把所有的value全部保存至一个列表中
print(list(dic.values()))

# 4.直接拿到字典中的key和value
print(dic.items())
for key,value in dic.items():
    print(key,value)

a,b =(1,2) # 元组和列表都可以，（解构）
print(a)
print(b)

#字典的嵌套
dic = {
    "name": "djh",
    "age": 21,
    "wife":{
        "name":"mldd",
        "age":21
    }
}

print(dic['wife']['age'])
dic['wife']['age'] = dic['wife']['age'] + 1
print(dic['wife']['age'])

# 循环删除
dic = {
    "da":"djh",
    "ma":"mldd",
    "dj":"wsdj"
}
temp = [] # 存放即将删除的key
for key in dic:
    if key.startswith("d"):
        temp.append(key)

for t in temp:
    dic.pop(t)

print(dic)