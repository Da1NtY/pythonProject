'''
假设列表 lst_info=[['李玉','男',25],['金忠','男',23],['刘妍','女',21],['莫心','女',24],['沈冲','男',28]]存放了某单位每个员工的基本信息。试编写程序，实现以下功能。
要求：
1）输出所有员工的姓名（要求用列表推导式完成）
2）输出年龄大于24的所有员工的信息（要求用列表推导式完成）
3）用户输入要删除的员工姓名，若该姓名在列表中存在，则执行删除操作，若不存在，则给出相应的提示。程序可循环执行，当用户输入姓名为“0”时，循环结束。

'''

# 员工信息列表
lst_info=[['李玉','男',25],['金忠','男',23],['刘妍','女',21],['莫心','女',24],['沈冲','男',28]]

# 员工姓名列表
lst_name = [lst_info[i][0] for i in range(0,len(lst_info))]
print(lst_name)

# 年龄大于24的所有员工的信息列表
lst_age24 = [lst_info[i] for i in range(0,len(lst_info)) if lst_info[i][2] > 24]
print(lst_age24)

while 1:
    name = str(input("请输入要删除的员工姓名："))
    if name == "0":
        break
    lst_name1 = [lst_info[i][0] for i in range(0, len(lst_info))]
    if name in lst_name1:
        for i in range(0,len(lst_info)-1):
            if lst_info[i][0] == name:
                lst_info.pop(i)
                print("删除成功！")
                lst_name1 = [lst_info[i][0] for i in range(0, len(lst_info))]
    elif name not in lst_name1:
        print("请输入正确的姓名！")
print(lst_info)