import qrcode

# 设置相关参数，生成一个二维码对象（QRcode对象）
qr_obj = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4
)

# 设置二维码信息内容
qr_obj.add_data('巴拉巴啦')

# 设置代表二维码信息量的矩阵大小
# 当参数fit为True时，二维码会根据信息内容大小选择合适的矩阵形式
# 当参数fit为Flash时，二维码不会改变矩阵大小，如果信息内容过大则报错
qr_obj.make(fit=True)

# 生成二维码图像
qr_img = qr_obj.make_image(fill_color="green", back_color="white")

# 显示二维码
qr_img.show()

# 保存二维码
qr_img.save('./test1.png')
