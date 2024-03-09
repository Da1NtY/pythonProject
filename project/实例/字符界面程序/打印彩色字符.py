def color_set(str, sel_color):
    # 前景色数值：31：红色，32：绿色，33：黄色，34：蓝色，35：紫红色，36：青蓝色，37：白色。
    # 生成一个颜色字典，保存控制颜色的转义序列
    # 这里只设置了前景色，背景色默认
    color_dic = {
        'red': '\033[31m',      #红色
        'green': '\033[32m',    #绿色
        'yellow': '\033[33m',   #黄色
        'blue': '\033[34m',     #蓝色
        'fuchsia': '\033[35m',  #紫红色
        'cyan': '\033[36m',     #青蓝色
        'white': '\033[37m',    #白色
        'normal': '\033[0m'     #终端默认颜色
    }
    # 把颜色参数sel_color转成小写
    sel_color = sel_color.lower()
    # 如果在字典color_dic中找到定义好的颜色值
    if sel_color in color_dic.keys():
        # 设置字符串的颜色
        return '%s%s%s' % (color_dic[sel_color],str, color_dic['normal'])
    else:
        print('没有找到对应颜色，采用终端默认颜色...')
        # 设置字符串默认颜色
        return '%s%s%s' % (color_dic['normal'], str, color_dic['normal'])

# 主函数
if __name__ == '__main__':
    # 设置字符串的颜色，并在终端上打印出来
    print(color_set('这一句是红色', 'red'))
    print(color_set('这一句是绿色', 'green'))
    print(color_set('这一句是黄色', 'yellow'))
    print(color_set('这一句是蓝色', 'blue'))
    print(color_set('这一句是紫红色', 'fuchsia'))
    print(color_set('这一句是终端默认颜色', 'test'))
