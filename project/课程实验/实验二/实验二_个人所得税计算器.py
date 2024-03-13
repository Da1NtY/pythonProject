'''
目前我国个人所得税的计算公式如下：
应纳个人所得税税额=（应发工资薪金所得-五险一金-个税免征额）*适用税率-速算扣除数
2018年10月1日起调整后，个人所得税免征额为 5000元/月，7级超额累进个人所得税税率表如下
全月应纳税所得额	        税率	速算扣除数
不超过3000元	            3	0
超过3000元至12000元的部分	10	210
超过12000元至25000元的部分	20	1410
超过25000元至35000元的部分	25	2660
超过35000元至55000元的部分	30	4410
超过55000元至80000元的部分	35	7160
超过80000元的部分	        45	15160
请编写一个个人所得税计算器，用户输入应发工资薪金所得、五险一金金额和个税免征额，
输出应缴税款和实发工资，结果保留小数点后两位。当输入数字小于0或等于0时，输出‘error’。
测试用例：
输入
请输入应发工资金额：16000
请输入五险一金金额：4000
请输入个人所得税免征额：5000
输出
应缴税款 490.00元，实发工资 11510.00元

'''

# 用户输入应发工资薪金所得、五险一金金额和个税免征额
wage = float(input("请输入应发工资金额："))
benefit = float(input("请输入五险一金金额："))
free_tax = float(input("请输入个人所得税免征额："))
while 1:
    if wage <= 0 or benefit <= 0 or free_tax <= 0:
        print("error")
        break
    before_submit = wage - benefit - free_tax
    if before_submit <= 3000:
        s_submit = before_submit*0.03
    elif 3000< before_submit <=12000:
        s_submit = 90 + (before_submit-3000)*0.1
    elif 12000< before_submit <=25000:
        s_submit = 990 + (before_submit-12000)*0.2
    elif 25000< before_submit <=35000:
        s_submit = 3590 + (before_submit-25000)*0.25
    elif 35000< before_submit <=55000:
        s_submit = 6090 + (before_submit-35000)*0.3
    elif 55000< before_submit <=80000:
        s_submit = 12090 + (before_submit-55000)*0.35
    elif 80000< before_submit:
        s_submit = 20840 + (before_submit-80000)*0.45

    real_wage = wage - s_submit

    # 输出应缴税款、实发工资
    print(f"应缴税款:{s_submit},实发工资:{real_wage}")
    break