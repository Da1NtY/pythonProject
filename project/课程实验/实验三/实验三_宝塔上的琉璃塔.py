'''
有一座八层宝塔，每一层都有一些琉璃灯，每一层的灯数都是上一层的两倍，已知共有765盏灯，计算并输出每层各有多少盏灯。
'''
# 总灯数
total_light = 765

# 层数
trip = 8

sum = 0
for i in range(trip):
    x = 2 ** i
    sum += x

first_light = total_light / sum

for i in range(trip):
    light = first_light * 2 ** i
    print(f"第{i+1}层有{light}盏灯")