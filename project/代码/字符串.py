#索引
s = "12345"
print(s[0])
#切片
#s[a:b:step] step步长默认是1
print(s[0:2])
print(s[-2:])
print(s[5:0:-1])

#字符串的常规操作
#字符串的操作一般不会对原字符串产生影响，一般是返回一个新的字符串

#字符串的大小写转换
p = "python"
p1 = p.capitalize() #首字母大写
print(p1)

p = "I love pyTHon"
p1 = p.title()  #单词的首字母大写
print(p1)

p1 = p.upper()  #把所有字母变成大写字母
print(p1)

p1 = p.lower()  #把所有字母变成小写字母
print(p1)

#如何忽略大小写来进行判断
verity_code = "aBcD"
user_input = input(f"请输入验证码：({verity_code})")
if verity_code.upper() == user_input.upper():
    print("验证码正确！")
else:
    print("验证码不正确！")

#替换和切割
s = "  1  2 2  "
s1 = s.strip() #去掉字符串两端的空格
print(s1)

#案例
username = input("请输入用户名：")
password = input("请输入密码：")
if username.strip() == "admin" and password.strip() == "123456":
    print("登录成功！")
else:
    print("登录失败！")

#字符串替换 replace(old,new)
s1 = s.replace(" ","")
print(s1)

#切割 用什么进行切割就会损失掉什么
a = "python_java_C"
lst = a.split("_") #用_来进行切割
print(lst)

#查找
s = "你好啊！我叫xxx"
ret = s.find("xxx") #如果返回-1，则没有。
ret1 = s.index("xxx") #如果没有则报错
print(ret)
print(ret1)
print("xxx" in s) #判断返回True或False
print("xxx" not in s)

#判断
name = input("请输入你的名字：")
if name.startswith("戴"): #判断字符串是否以XXX开头  endswith() 结尾
    print("你姓戴")
else:
    print("你不姓戴")

money = input("请输入你兜里的钱：")
if money.isdigit(): #判断字符串是否由整数组成
    money = int(money)
    print("你可以花钱了！")
else:
    print("你输入有误！")

s = "hello"
print(len(s)) #len()长度

lst = ["1","2","3"]
s = "_".join(lst) #连接
print(s)
