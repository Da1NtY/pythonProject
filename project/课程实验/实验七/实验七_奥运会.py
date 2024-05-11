'''
已知2012年奥运会体育运动员名单如下
女子；程菲（跳马、自由体操、平衡木）、杨伊琳（高低杠、个人全能）、何可欣（高低杠）、江钰源（自由体操、跳马、个人全能）、李珊珊（平衡木）、邓琳琳（平衡木、跳马、自由体操）
男子；杨威（个人全能）、李小鹏（双杠、跳马、自由体操）、肖钦（鞍马）、黄旭（双杠、鞍马）、陈一冰（吊环）、邹凯（自由体操）
要求分别用集合运算、集合方法显示如下信息，并进行检验。
（1）男子体操项目和项目数；女子体操项目和项目数
（2）所有体操项目和项目数
（3）男、女独有的项目和项目数
'''
# 女子体操运动员和项目
female_athletes = ['程菲（跳马、自由体操、平衡木）', '杨伊琳（高低杠、个人全能）', '何可欣（高低杠）',
                   '江钰源（自由体操、跳马、个人全能）', '李珊珊（平衡木）', '邓琳琳（平衡木、跳马、自由体操）']
female_events = set()
for athlete in female_athletes:
    events = athlete.split('（')[1].split('、')
    female_events.update(events)

# 男子体操运动员和项目
male_athletes = ['杨威（个人全能）', '李小鹏（双杠、跳马、自由体操）', '肖钦（鞍马）',
                 '黄旭（双杠、鞍马）', '陈一冰（吊环）', '邹凯（自由体操）']
male_events = set()
for athlete in male_athletes:
    events = athlete.split('（')[1].split('、')
    male_events.update(events)

# (1) 男子体操项目和项目数；女子体操项目和项目数
print("男子体操项目:", male_events)
print("男子体操项目数:", len(male_events))
print("女子体操项目:", female_events)
print("女子体操项目数:", len(female_events))

# (2) 所有体操项目和项目数
all_events = male_events.union(female_events)
print("\n所有体操项目:", all_events)
print("所有体操项目数:", len(all_events))

# (3) 男、女独有的项目和项目数
male_only_events = male_events.difference(female_events)
female_only_events = female_events.difference(male_events)
print("\n男子独有项目:", male_only_events)
print("男子独有项目数:", len(male_only_events))
print("女子独有项目:", female_only_events)
print("女子独有项目数:", len(female_only_events))