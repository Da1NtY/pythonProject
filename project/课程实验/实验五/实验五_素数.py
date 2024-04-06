'''
神奇的素数
1）编写判断m是否为素数的函数fun(m),若m是素数则返回True;否则返回False。
2）编写判断m是否是回文数的函数palindrome(m) ,
若m是回文数则返回True;否则返回False。
3）找出2~100中的所有孪生素数。孪生素数是指相差2的素数对，
如3和5、5和7、11和13等。
4）找出2~100中的所有反素数。反素数是指将其逆向拼写后也是素数的非回文数。
   例如：17和71都是素数且均不是回文数，所以17和71都是反素数
5）输出2～100范围内的所有的回文素数。
6）将4~20中所有的偶数分解成两个素数的和。例如，6=3+3、8=3+5、10=3+7
'''
# 判断素数
def fun(m):
    for i in range(2,m):
        if m % i == 0:
            return False
    return True

# 判断回文数
def palindrome(m):
    s = str(m)
    return s == s[::-1]

# 寻找孪生素数
def twinborn_fun(a,b):
    twin_lst = []
    for i in range(a,b):
        if fun(i) and fun(i+2) :
            twin_lst.append((i,i+2))
    return twin_lst

#寻找反素数
def against_fun(a,b):
    a_list = []
    for i in range(a,b):
        if fun(i) and not palindrome(i):
            index = int(str(i)[::-1])
            if fun(index):
                a_list.append(i)
    return a_list

# 寻找回文素数
def palindrome_fun(a,b):
    palindrome_fun_list = []
    for i in range(a,b):
        if fun(i) and palindrome(i):
            palindrome_fun_list.append(i)
    return palindrome_fun_list

# 偶数分解成两个素数的和
def sum_of_fun(a,b):
    result = []
    for i in range(a,b+1,2):
        for j in range(2,i):
            if fun(j) and fun(i-j):
                result.append(f"{i}={j}+{i-j}")
                break
    return result

# 找出2~100中的所有孪生素数
print(twinborn_fun(2,100))

# 找出2~100中的所有反素数
print(against_fun(2,100))

# 输出2～100范围内的所有的回文素数
print(palindrome_fun(2,100))

# 将4~20中所有的偶数分解成两个素数的和
print(sum_of_fun(4,20))
