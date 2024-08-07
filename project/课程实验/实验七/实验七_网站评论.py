'''
用列表保存网站评论，写一个程序过滤重复字超过一定比例（70%）的评论，并分别以字符串方式输出原评论和过滤后的评论。
【提示】：
每个评论是一个字符串，多个评论放在列表中，可用filter()函数对列表中的每个字符串s进行过滤。过滤规则是：字符串中不重复的字符数（len(set(s))）在原字符串字符数（len(s)）的占比超过70%，则是有效字符串（评论）。

测试数据：comments = ['这是一本非常好的书，作者用心了',
           '作者大大辛苦了',
           '好书，感谢作者提供了这么多的好案例',
           '啊啊啊啊啊啊，我怎么才发现这么好的书啊，相见恨晚',
           '好好好好好好好好好好好',
           '好难啊看不懂好难啊看不懂好难啊看不懂',
           '书的内容很充实',
           '物超所值，好书，赞一个',
           '32个赞赞赞赞赞赞赞赞赞赞赞赞赞赞赞赞赞赞赞赞赞赞赞赞赞赞赞赞赞赞赞赞',
           '你的书上好多代码啊，不过想想也是，编程的书嘛，肯定代码多一些',
           '书很不错!!一级棒!!买书就上当当，正版，价格又实惠，让人放心!!! ',
           '无意中来到你小铺就淘到心意的宝贝，心情不错! ',
           '送给朋友的、很不错',
           '老师让买的，果然不错，没有让我失望']

'''
def filter_comments(comments, threshold=0.7):
    filtered_comments = []
    for comment in comments:
        unique_chars = len(set(comment))
        total_chars = len(comment)
        if unique_chars / total_chars >= threshold:
            filtered_comments.append(comment)
    return filtered_comments

# 测试数据
comments = ['这是一本非常好的书，作者用心了',
            '作者大大辛苦了',
            '好书，感谢作者提供了这么多的好案例',
            '啊啊啊啊啊啊，我怎么才发现这么好的书啊，相见恨晚',
            '好好好好好好好好好好好',
            '好难啊看不懂好难啊看不懂好难啊看不懂',
            '书的内容很充实',
            '物超所值，好书，赞一个',
            '32个赞赞赞赞赞赞赞赞赞赞赞赞赞赞赞赞赞赞赞赞赞赞赞赞赞赞赞赞赞赞赞赞',
            '你的书上好多代码啊，不过想想也是，编程的书嘛，肯定代码多一些',
            '书很不错!!一级棒!!买书就上当当，正版，价格又实惠，让人放心!!! ',
            '无意中来到你小铺就淘到心意的宝贝，心情不错! ',
            '送给朋友的、很不错',
            '老师让买的，果然不错，没有让我失望']

print("原评论:")
for comment in comments:
    print(comment)

print("过滤后：")
filtered_comments = filter_comments(comments, threshold=0.7)
for comment in filtered_comments:
    print(comment)