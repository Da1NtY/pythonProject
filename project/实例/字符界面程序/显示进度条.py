import sys
# 导入进程暂停包
from time import sleep
# 定义一个进度条类，对进度条属性和功能进行封装
class ProgressBar(object):
    # 初始化函数，设置进度条的总长度，初始长度，组成进度条的字符
    def __init__(self,len,bar_char='$'):
        # 初始化进度条的总长度
        self.total_len = len
        # 设置组成进度条的字符
        self.bar_char =bar_char
        # 设置进度条起始长度为0
        self.cur_len = 0
        # 把终端输出对象sys.stdout 赋值给 self.write_direction
        self.write_direction = sys.stdout
        # 如果未给出进度条总长度赋值，直接退出
        if not self.total_len:
            return
        # 设置vstr为45个"-"
        vstr ='-'*45
        # 在终端上打印相关信息，等价于：print('\n'+ vstr + '进度条演示' + vstr)
        self.write_direction.write('\n'+ vstr + '进度条演示' + vstr)

    # 显示进度条的函数，show_len是进度条最新长度
    def show(self,show_len):
        # 如果进度条最新长度大于进度条总长度，设置进度百分比为100
        if show_len>self.total_len:
            percent_int =100
        else:
            # 取得进度条最新长度与进度条总长度的百分比的整数值
            percent_int =(show_len*100)//self.total_len
        # 要显示的进度条，这个进度条由percent_int个self.bar_char()组成
        cur_string = ("%s"%(self.bar_char)) * percent_int
        # 进度条与后面要显示的百分比之间的内容，由（100 - percent_int）个空格组成
        blank = ' ' * (100 - percent_int)
        # 通过sys.stdout 对象的write()函数向终端写入内容（内容暂时存在内存里）
        # \r 表示从当前开头重新覆盖地写
        self.write_direction.write('\r' + cur_string + blank + str(percent_int) + '%')
        # 通过flush()函数将内存的内容写到终端上
        self.write_direction.flush()
        # 将传入的进度条长度保存在self.cur_len中
        self.cur_len = show_len
        # 如果长度达到总长度，传入回车字符进行换行
        if percent_int == 100:
            self.write_direction.write("\n")

    # 处理进度条每次增加长度的函数，new_len是每次增加的长度
    def add_bar_len(self,new_len):
        # 将进度条当前长度增加到new_len
        self.cur_len = self.cur_len + new_len
        # 显示进度条
        self.show(self.cur_len)

    # 主函数main
if __name__ == "__main__":
    # 实例化进度条类，生成进度条对象，并设置总长度为200
    progressbar_obj = ProgressBar(len = 200)
    # 循环20次，每增加10，完成循环后，长度正好为200
    for i in range(20):
        sleep(0.6)
        # 每次增加长度10
        progressbar_obj.add_bar_len(10)