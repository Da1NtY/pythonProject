'''
4.假设已有列表
lst=[('triangle','shape'),('red','color'),('square','shape'),('yellow','color'),('green','color'),('circle','shape')]
其中每个元素都是一个元组。元组中的第一个元素表示值，第二个元素表示标签。试编写程序，完成以下功能：
1）将列表lst中的元素按照标签排序后输出
2）将所有的颜色值从列表lst中提取出来，存入列表lst_colors,并将该列表输出。
'''
lst=[('triangle','shape'),('red','color'),('square','shape'),('yellow','color'),('green','color'),('circle','shape')]
# 将列表lst中的元素按照标签排序后输出
sorted_lst = sorted(lst, key=lambda x: x[1])
print("按标签排序后的列表：", sorted_lst)

# 将所有的颜色值从列表lst中提取出来，存入列表lst_colors,并将该列表输出
lst_colors = [item[0] for item in lst if item[1] == 'color']
print("提取的颜色值：", lst_colors)