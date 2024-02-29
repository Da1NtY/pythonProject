# #while循环
# a = input("请输入a的值")
# a = int(a)
# while a > 10:
#     a=a-1
#     print(a)
#     # break

# #作业题 1+2-3+4-5·····+5050=？
# a = int(input("请输入a的值："))
# i=1
# s=1
# while i < a:
#     i = i + 1
#     if (i%2) == 0:
#         s = s + i
#     else:
#         s = s - i
# print(s)


#for循环
s = "你好啊，我叫赛利亚"

for i in s:
    print("这一次循环得到的是", i)

# for i in range()
# range(n):从0数到n,不包含n
# range(m,n):从m数到n,不包含n
# range(m,n,s):从m数到n,不包含n,每次的间隔为s