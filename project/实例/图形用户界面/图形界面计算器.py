import tkinter as  tk

# 单击按键调用的函数
def cal_command(event):
    # 取得计算器按键上的文本
    but_text = event.widget['text']
    # 如果单击了等号键，取得计算式的值
    if but_text == '=':
        try:
            # 通过eval()函数取得计算器的值，并转换成字符串
            resulut_num = str(eval(show_text.get()))
            but_text_new = resulut_num
        except:
            # eval()函数无法取得计算式的值，如计算式错误
            show_text.set('录入有错，单击C键清除')
            return
    elif but_text == 'C':
        but_text_new = ''
    else:
        # 如单击了数值键、运算符键，该键值追加在显示框中已有字符串后面
        but_text_new = show_text.get() + but_text

    # 在显示框中显示
    show_text.set(but_text_new)

# 计算器按钮排列函数
def layout():
    txt = ['7','8','9','+','C','4','5','6','-','%','1','2','3','*','=','0','.','/']

    # 保存列表中的索引
    but_index = 0
    # 设置计算器的按键，i设置按键列所在行
    for i in range(1,5):
        # 超出列表的索引值，退出
        if but_index >= 18:
            break
        # j设置按键排列所在的列
        for j in range(0,5):
            if but_index >=18:
                break
            # 生成计算器上的按键，是一个Button控件
            bt = tk.Button(text=txt[but_index], width=12, height=1)

            # 当按键值为“=”时，设置等号按键高度跨两行
            if txt[but_index] == '=':
                bt.config(width=12, height=3)
                bt.grid(row=i, column=j, rowspan=2)
            # 当按键值为0时，设该按键宽度跨两列
            elif txt[but_index] == '0':
                bt.config(width=25)
                bt.grid(row=i, column=j, columnspan=2)
            # 由于前面的按键0跨两列，后面的“.”和“/”键依次向后顺延一列
            elif txt[but_index] == '.' or txt[but_index] == '/':
                bt.grid(row=i, column=j+1)
            else:
                # 其他按键按行和列正常排放
                bt.grid(row=i, column=j)
            # 事件绑定，设置鼠标单击时，调用cal_command()函数
            bt.bind('<Button-1>', cal_command)
            # 添加索引值
            but_index +=1


# 主函数
if __name__ == '__main__':
    # 生成一个窗口
    win = tk.Tk()
    # 设置窗口
    win.title("计算器")
    show_text = tk.StringVar(value='')
    # 用Label控件做计算器显示框
    # relief设置控件浮雕样式 ，属性有：FLAT、RAISED、SUNKEN、GROOVE和RIDGE等
    # borderwidth设置边框宽度，通过anthor = tk.SE设置控件锚点在右下角
    lab = tk.Label(win, relief=tk.SUNKEN, borderwidth=3, anchor=tk.SE)

    # 设置背景色，通过textvariable=show_text将控件的text属性与变量show_text绑定
    lab.configure(background='white', textvariable=show_text, height=2, width=66)

    # 把控件摆放在表格中，sticky是对其方式
    lab.grid(row=0, column=0, columnspan=5, sticky=tk.SW)

    layout()
    # 显示窗口
    win.mainloop()