s = "周杰伦"
bs1 = s.encode("gbk")  # byte类型
bs2 = s.encode("UTF-8")
print(bs1)
print(bs2)

# 怎么把一个gbk的字节转换成utf-8的字节
# 先变成字符串
# str.encode("编码")  进行编码
# bytes.decode("编码")  重新编码
bs = b'\xd6\xdc\xbd\xdc\xc2\xd7'
s = bs.decode("gbk")
bs2 = s.encode("UTF-8")
print(bs2)

s = "你好abc"
print(s.encode("utf-8"))