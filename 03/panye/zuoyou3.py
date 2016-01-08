
read_me = ''' first of all, i want make it clear that i can not claim understanding this holy book in just a few weeks, and i would not dare comment on this sacred book, in addition, i don't think i can give you a full picture of the holy bible in just few words.i can not preach anything here. what i want to do here is to express my understanding by sharing two events described in this book. the fist story i want to share is abandoned tower of babel.according to the bibel,people use the same language to communicate with each other in ancient times.with the soaring vanity,they decided to build a heaven-reaching tower to show off their achievement, god knows, he change the human language into different kinds and make it difficult for people to communicate with each other,hence the failure of building tower of babel.this story tells people,never do things in selfishness, but make a life out of enternal glory.the other story,before jesus christ was crucified,he said, father,forgive them, for they know not what they do. with great love, he shouldered all the sins of people. what can we learn from this story?we live in this world thanks to the love of god, for this reanson, we should make our lives glorious to honor our god.finally,i want to sum up by saying that only if we put our lives in the eternal love of god,can we live a perfect life, and what you appealed is what god expected! '''

words = {}

for i in read_me:
    words.setdefault(i,0)
    words[i] += 1

_tolist = words.items()
for t in range(len(_tolist)-1, -1, -1):
    for i in range(t):
        if _tolist[i][1] < _tolist[i+1][1]:
            _tolist[i], _tolist[i+1] = _tolist[i+1],  _tolist[i]
#print _tolist

print _tolist[:11]

'''
不错
使用dict对字符串中的字符计数
使用setdefault初始化字符个数
使用冒泡排序对每个元素的都是tuple的list进行从大到小排序
使用切片获取排序后列表的前十位

继续加油，可以在完成的基础功能之上给自己添加点障碍
比如如果前20个字符的数量都相同呢？我们可以指定一个规则比如按字母a到z的顺序找到前10个
比如如果read_me中有大小写的字符呢？我们不区分大小写时如何统计


'''