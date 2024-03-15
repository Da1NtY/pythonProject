import tkinter as tk
# 导入图片操作模块
from tkinter import PhotoImage
# 建立一个窗口
win = tk.Tk()
win.title("这是一个窗口")

# 设置窗口宽300，高200像素，离屏幕左侧30像素，离屏幕顶部20像素
win.geometry('300x200+30+10')

# 在窗口中加一个Label控件lb_test，参数win是Laabel控件所在窗口
# 参数text指定Label的文本内容
lb_test = tk.Label(win, text="这是一个窗口！", font=("宋体", 12), fg="red", bg="green")

# 在窗口上放置label控件，pack()是一种控件放置方式
# 参数pady设置控件在纵向上的边距，一般用于非精确位置摆放
lb_test.pack(pady = 20)

# 在程序当前目录添加GIF格式的图片
img = PhotoImage(file='./test.png')

# 在窗口中加一个Label控件lb_img，参数win是Label控件所在窗口
lb_img = tk.Label(win, image=img)

# 在窗口底部放置控件
lb_img.pack(side=tk.BOTTOM)

# 显示窗口
win.mainloop()
