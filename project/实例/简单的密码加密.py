# 形成密码前缀，实现方式是对密码中每个字符进行转换得到一个新字符串
def passwd_pre(pwd):
    vret = []
    # 取得密码的每一个字符，通过以下方式转换为另一个字符
    for char in pwd:
        if char in 'abc':
            char = '!'
        elif char in 'def':
            char = '@'
        elif char in 'ghi':
            char = '#'
        elif char in 'jkl':
            char = '%'
        elif char in 'mno':
            char = '^'
        elif char in 'pqr':
            char = '&'
        elif char in 'stu':
            char = '*'
        elif char in 'vwx':
            char = '>'
        elif char in 'yz':
            char = '?'
        elif char in 'Z':
            char = 'a'
        elif char.isupper():
            # 对于大写字母，先通过char.lower()将其转换成小写字母，然后转成16位数值并加1，
            # 最后再转换成字母，即把当前的大写字母转换成该字母的下一个字母的小写形式
            char = chr(ord(char.lower()) + 1)

        # 把转换后的字符加入到vret列表变量中去
        vret.append(char)

        # 把列表中各项连接成字符串并返回
        return ''.join(vret)

# 该函数根据传入的密码和两个字符串，对密码中的字符进行转换
# 主要功能是根据密码pwd中的每个字符，在字符串str1中找到对应的位置索引，
# 通过这个索引值在字符串str2中找到一个字符替换密码中的字符
def change_txt(pwd, str1, str2):
    # 初始化返回值
    vret = ''
    # 将字符串转换为小写
    pwd = pwd.lower()
    for char in pwd:
        # 取得在str1中的索引值
        j = str1.find(char)
        # 在str1中没有这个字符，就返回-1
        if j == -1:
            # 没有找到索引值，就保留字符原值
            vret = vret + char
        else:
            # 找到索引值，根据这个索引值在str2中取一个字符代替原字符
            vret = vret + str2[j]
    return vret

# 加密程序
def change_password(pwd):
    if pwd == None:
        return '-1'
    vret = ''
    # 取得一个字符串，作为转换后密码的前缀
    vpre = passwd_pre(pwd)
    vlen = len(pwd)
    # 调用函数对密码进行一次转换，函数的后两个参数决定返回的内容
    vstr = change_txt(pwd, "1234567890abcdefghijklmnopqrstuvwxyz", "abcdefghijklmnopqrstuvwxyz1234567890")
    if vlen <= 4:
        vret = vpre + vstr[0:vlen]
    else:
        vret = vpre + vstr[0:4]
    # 调用函数对密码进行一次转换
    vstr = change_txt(pwd, "1234567890abcdefghijklmnopqrstuvwxyz", "qwertyuiopasdfghjklmnbvcxz0987654321")
    if vlen <= 4:
        vret = vret + vstr[0:vlen]
    else:
        vret = vret + vstr[0:4]
    # 调用函数对密码进行一次转换
    vstr = change_txt(pwd, "1234567890abcdefghijklmnopqrstuvwxyz", "1qaz2wsx3edc4rfv5tgb6yhn7ujm8ik9ol0p")
    if vlen <= 4:
        vret = vret + vstr[0:vlen]
    else:
        vret = vret + vstr[0:4]
    # 调用函数对密码进行一次转换
    vstr = change_txt(pwd, "1234567890abcdefghijklmnopqrstuvwxyz", "pl0okm9ijn8uhb7ygv6tfc5rdx4esz3wa2q1")
    if vlen <= 4:
        vret = vret + vstr[0:vlen]
    else:
        vret = vret + vstr[0:4]
    return vret

# 主函数main
if __name__ == '__main__':
    while True:
        pwd = input('请录入密码：')
        if pwd == 'q':
            print('退出程序.......')
            break
        else:
            pwdnew = change_password(pwd)
            print('您录入的密码是：', pwd, '该密码加密后是：', pwdnew)