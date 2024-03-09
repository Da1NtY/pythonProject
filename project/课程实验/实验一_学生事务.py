'''
已知第一学期必修课程及其学分如下：
Python 3学分，高等数学 4学分，大学英语 4学分，大学体育 2学分，军事理论 2学分，哲学 2学分
1）输入每学分应缴纳的学费，计算并输出第一学期应缴纳多少学费.
2）输入你每个月的生活费，计算你每学期能够贷款的金额（结果保留小数点后2位数字）
   每学期按5个月计算，可以申请的额度不超过学费和生活费的60%

'''

# 学分
credit_Python = 3
credit_Math = 4
credit_English = 4
credit_PE = 2
credit_Ac = 2
credit_Fhli = 2

# 总学分
credit_sum = credit_Python + credit_Math + credit_English + credit_PE + credit_Ac + credit_Fhli

# 输入每学分应缴纳的学费
credit_price = float(input("请输入每学分应缴纳的学费："))

# 输出第一学期选修学分
print("你本学期选修了{}个学分".format(credit_sum))
# 输出第一学期应缴纳多少学费
print("第一学期应缴纳的学费为{}".format(round(credit_sum*credit_price,2)))

# 输入你每个月的生活费
month_livingcost = float(input("输入你每个月的生活费："))

# 输出你每学期能够贷款的金额
tuiton = credit_sum*credit_price
print("你本学期能够贷款的金额为：{}".format(round((month_livingcost*5+tuiton)*0.6,2)))