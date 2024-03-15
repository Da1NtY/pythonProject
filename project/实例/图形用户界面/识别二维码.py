import pyzbar.pyzbar as pyzbar
from PIL import Image

# 二维码图片文件的路径
qrcode_img = './test1.png'

# 读入文件
img = Image.open(qrcode_img)

# 将图片转换成灰度图，这样利于二维码的识别
img = img.convert('L')

# 对图片img中的二维码进行解码，返回值是一个列表
# 列表中的元素项是识别出来的二维码对象
# 它的data属性是二维码的信息内容
list_qrobj = pyzbar.decode(img)
# 通过循环取出每个二维码对象
for qrobj in list_qrobj:
    # 打印出二维码内容
    print(qrobj.data.decode("UTF-8"))