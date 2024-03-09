# 导入相应的模块
import pandas as pd
from pandas import DataFrame, Series
import numpy as np

# 生成一个DataFrame对象，DataFrame对象由字典类型数据转换而成
# 字典的每个键值是一个列表类型
emp_info = DataFrame(data = {
    "姓名":["张三","李四","王五","赵六","赵七","钱八"],
    "物理":np.random.randint(0,100,size=6),
    "化学":np.random.randint(0,100,size=6),
    "数学":np.random.randint(0,100,size=6)},
    index = np.arange(1,7))
# print(emp_info)
# 保存为Excel文件，DataFrame类型的数据可以直接保存到Excel文件中
emp_info.to_excel("./emp.xlsx")

# 打开该文件，并把第一列设为索引，用index_col = 0 设置
# pandas模块的read_excel()可以直接读取Excel数据
vfile = pd.read_excel('./emp.xlsx',index_col=0)

#将文件的内容读入到DataFrame对象df中
df = pd.DataFrame(vfile)

# axis = 1表示按行的方向进行计算，这里sum(axis=1)表示将同一行的数据进行求和
sum_score = df.sum(axis=1)

# 按行求平均分值
avg_score = df.mean(axis=1)

# 最后增加“总分”和“平均分”列，防止新计算出的列值参与到DataFrame对象中的运算
# 在DataFrame对象的df中增加一个“总分”列，用来保存每位成员的成绩总分
df["总分"] = sum_score

# 在DataFrame对象的df中增加一个“平均分”列，用来保存每位成员的成绩平均分
df["平均分"] = avg_score

# 将DataFrame对象df数据保存到文件中
df.to_excel('./emp.xlsx')