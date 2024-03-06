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