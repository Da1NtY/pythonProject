'''
装饰器：
    在不改变原有函数调用的情况下，给函数增加新的功能

    用处： 用户登录、日志

    格式：
    def wrapper(fn):              wrapper： 装饰器    fn： 目标函数
        def inner(*args, **kwargs):
            # 在目标函数执行之前
            fn(*args, **kwargs)
            # 在目标函数执行之后
        return inner       千万别加小括号
'''
# def guanjia(game):
#     def inner():
#         print("打开外挂")
#         game()
#         print("关闭外挂")
#     return inner
#
# @ guanjia
# def lol():
#     print("德玛西亚！！！！！")
#
# @ guanjia
# def csgo():
#     print("来b下包！")
#
# lol()
# csgo()

def guanjia(game):
    def inner(*args, **kwargs): # *，**表示接受所有参数，打包成元组和字典
        print("打开外挂")
        game(*args,**kwargs)  # *，**表示把args元组和kwargs字典打散成 位置参数以及关键字参数传递进去
        print("关闭外挂")
    return inner

@ guanjia
def lol(username,password,hero):
    print("欢迎召唤师",hero)
    print("德玛西亚！！！！！")

@ guanjia
def csgo(username,password,area):
    print(f"来{area}下包！")

lol("username","password","大盖伦")
csgo("123","password","a")