# 判断字符串长度是否在 8 位以上
def check_len(pwd):
    if len(pwd) >= 8:
        return True
    else:
        return False

# 检查字符串是否是由大小写字母、数字、其他符号组成
def check(pwd):
    # 初始化一个列表变量
    check = [0,0,0,0]
    for char in pwd:
        # 如果字符是小写，将check[0]置为1
        if char.islower():
            check[0] = 1

        # 如果字符是大写，将check[1]置为1
        if char.isupper():
            check[1] = 1

        # 如果字符是数字，将check[2]置为1
        if char.isdigit():
            check[2] = 1

        # 如果字符是其他字符，将check[3]置为1
        if not (char.isalpha() | char.isdigit() | char.isspace()):
            check[3] = 1

    # 当列表中4个元素的值之和为4，则说明字符串符合四个条件
    if sum(check) < 4:
        return False
    else:
        return True

# 检查字符串是否包含重复的、四位以上的子串
# 只判断4位的子串是否有重复
# 考虑到密码的组成规则，当4位以上的子串重复时，必定有4位的子串重复
def check_rep(pwd):
    n = len(pwd)
    # 通过循环依次取出4个字符组成的子串
    # 只要它后面的字符串包含有一个这样的子串，重复就为真
    for i in range(n-4):
        # 取4个字符组成子串str1
        str1 = pwd[i:i + 4]
        # 取在str1后的剩余所有子串作为str2
        str2 = pwd[i + 4::]
        # 如果在str2中存在一个str1，说明重复
        if str1 in str2:
            return False
    return True

# 主函数
if __name__ == '__main__':
    msg = '''
    请设置密码，密码要求符合以下条件
    1.密码长度不小于8位
    2.密码必须由大小写字母、数字、其他符号组成
    3.密码中不能重复包含长度超过4的子串
    '''
    print(msg)
    while True:
        # 提示输入密码
        pwd = input('请录入密码：')
        # 如果录入q，退出程序
        if pwd == 'q':
            print('退出程序.........')
            break
        # 调用函数检查密码的位数
        vcheck1 = check_len(pwd)
        if not vcheck1:
            print('密码长度不够8位！请重新输入\n')
            continue

        # 调用函数检查密码是否由大小写字母、数字和其他符号组成
        vcheck2 = check(pwd)
        if not vcheck2:
            print('密码必须由大小写字母、数字和其他符号组成！请重新输入\n')
            continue

        # 调用函数检查密码是否有重复子串
        vcheck3 = check_rep(pwd)
        if not vcheck3:
            print('密码包含两个以上重复子串（4位以上的子串）！请重新输入\n')
            continue

        print('密码正确！')
        break