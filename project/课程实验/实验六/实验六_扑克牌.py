'''
假设列表lst_suit=['黑桃','红桃','梅花','方块']，存放了扑克牌的花色。
列表lst_face=['3','4','5','6','7','8','9','10','J','Q','K','A','2'],
存放了扑克牌的牌面大小,其元素已按照牌面大小升序排列。试编写程序，完成以下功能。
1）利用列表推导式，存放所有牌面（不考虑大小王）。新列表lst的内容为
[3黑桃 3红桃 3梅花 3方块 4黑桃 4红桃 4梅花 4方块...A黑桃 A红桃 A梅花 A方块 2黑桃 2红桃 2梅花 2方块]
2)使用random库的shuffle()函数将列表lst中的元素次序打乱
3)将用户抽取的牌面与计算机抽取的牌面进行大小比较（不考虑花色），并将结果输出。三种输出内容对照如下：
“恭喜，您赢了！”
“很遗憾，您输了！”
“咱们平手！”
'''
import random

lst_suit = ['黑桃', '红桃', '梅花', '方块']
lst_face = ['3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A', '2']

# 利用列表推导式，存放所有牌面（不考虑大小王）
lst = [f'{face}{suit}' for suit in lst_suit for face in lst_face]
print("所有牌面：", lst)

# 使用random库的shuffle()函数将列表lst中的元素次序打乱
random.shuffle(lst)
print("打乱后的牌面：", lst)

# 将用户抽取的牌面与计算机抽取的牌面进行大小比较（不考虑花色），并将结果输出
user_card = lst.pop()
computer_card = lst.pop()

user_face = user_card[:-2]
computer_face = computer_card[:-2]
print(f"用户为{user_card}")
print(f"电脑为{computer_card}")

if lst_face.index(user_face) > lst_face.index(computer_face):
    print("恭喜，您赢了！")
elif lst_face.index(user_face) < lst_face.index(computer_face):
    print("很遗憾，您输了！")
else:
    print("咱们平手！")