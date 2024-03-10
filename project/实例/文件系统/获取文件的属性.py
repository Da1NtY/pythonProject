# 导入时间模块
import time
# 导入操作系统模块
import os
# 将时间戳转化为中文时间格式
def timestamp_to_string(timestamp):
    # 将时间戳转化为本地的时间戳
    vtime = time.localtime(timestamp)
    # 将时间戳转换为中文时间格式
    vdatetime = time.strftime("%Y-%m-%d %H:%M:%S", vtime)
    return vdatetime
# 将字节数化为以M为计量单位的数值
def bytetoM(size):
    vsize = size/float(1024*1024)
    return round(vsize,2)

# 主函数
if __name__ == '__main__':
    # 通过os.stat()函数取得文件的信息
    fileinfo = os.stat("C:/Users/28360/Desktop/A110.xlsx")
    print("文件信息：")
    print('文件建立时间：',timestamp_to_string(fileinfo.st_ctime))
    print("文件的大小：",bytetoM(fileinfo.st_size),'M')
    print('文件修改时间：',timestamp_to_string(fileinfo.st_mtime))
    print("文件访问时间：",timestamp_to_string(fileinfo.st_atime))