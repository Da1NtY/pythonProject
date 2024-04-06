'''
编写一个函数，简单模拟微信发红包算法。
函数有两个参数，一个参数表示红包总金额，默认为100；另一个参数表示红包数量，默认值为15.
所有随机产生的红包金额（保留两位小数）存放在一个列表，并作为函数的返回值。
在主程序中测试该函数，要求对函数的默认值也进行测试。

红包的基本要求
1）所有人抢到的金额之和等于红包总额
2）每个人至少抢到0.01元

【提示】
设定总金额为100元，有N个人随机领取：
N=1 ，第一个红包金额=0.01至100-0.01之间的某个随机数。
N=2 ，第二个红包金额=0.01至（100-红包1）-0.01之间的某个随机数。
N=3 ，第三个红包金额=0.01至（100-红包1-红包2）-0.01之间的某个随机数。
每次运算时，在[0.01,剩余金额-0.01）之间产生一个随机数

为了使每个人抢到的红包金额不要太大，可以改进以下，采用二倍均值拆包
每次运算时，可在[0.01,剩余金额/剩余个数*2）之间产生一个随机数

为保证总数一致，先随机产生14个红包，最后一个红包用总数减

'''
import random
def send_packet(total_amount,number):
    amount_list = []
    remain_amount = total_amount

    # 生成number-1个红包的金额
    for i in range(number-1):
        max_amount = remain_amount / (number - i) * 2 * 0.99
        red_packet_amount = round(random.uniform(0.01,max_amount),2)
        amount_list.append(red_packet_amount)
        remain_amount = remain_amount - red_packet_amount

    # 最后一个红包
    amount_list.append(round(remain_amount,2))
    return amount_list

packet_list = send_packet(100,15)
print(packet_list)
