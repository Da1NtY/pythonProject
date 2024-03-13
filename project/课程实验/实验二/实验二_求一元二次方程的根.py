'''
输入一元二次方程的三个系数a,b,c，输出两个实根x1和x2，若没有实根则输出信息“无实根”。
'''
import math

a = int(input("请输入一元二次方程的系数a:"))
b = int(input("请输入一元二次方程的系数b:"))
c = int(input("请输入一元二次方程的系数c:"))

# 对有无实根进行判断
if b**2 - 4*a*c >= 0:
    x1 = (-1*b+ math.sqrt(b**2-4*a*c))/2/a
    x2 = (-1*b- math.sqrt(b**2-4*a*c))/2/a
    print(f"x1={x1},x2={x2}")
else:
    print("方程无实根")