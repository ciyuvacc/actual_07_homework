#!/usr/bin/env python
#coding=utf-8
_string = """
first of all, i want make it clear that i can not claim understanding this holy book  in just a few weeks, and i would not dare comment on this sacred book, in addition, i don't think i can give you a full picture of the holy bible in just few words.i can not preach anything here. what i want to do here is to express my understanding by sharing two events described in this book. the fist story i want to share is abandoned tower of babel.according to the bibel,people use the same language to communicate with each other in ancient times.with the soaring vanity,they decided to build a heaven-reaching tower to show off their achievement, god knows, he change the human language into different kinds and make it difficult for people to communicate with each other,hence the failure of building tower of  babel.this story tells people,never do things in selfishness, but make a life out of enternal glory.the other story,before jesus christ was crucified,he said, father,forgive them, for they know not what they do. with great love, he shouldered all the sins of  people. what can we learn from this story?we live in this world thanks to the love of god, for this reanson, we should make our lives glorious to honor our god.finally,i want to sum up by saying that only if we put our lives in the eternal love of god,can we live a perfect life, and  what you appealed is what god expected!
"""
_dict = {}
for _key in _string:   # 把字符以key,value 的形式存放在字典中
    _dict.setdefault(_key,0)
    _dict[_key] += 1

_dict = _dict.items()   # 把dict转换成list
print "未更改的list"
print _dict
for j in range(len(_dict) -1 ):
    for i in range(len(_dict) -1 ):
        if _dict[i][1] < _dict[i+1][1]:   #  条件1： 比较字符出现的次数比后面小的直接替换
            _dict[i],_dict[i+1] = _dict[i+1],_dict[i]
        elif _dict[i][0] > _dict[i+1][0] and _dict[i][1] == _dict[i+1][1]:  #条件2：当出现的次数一样的情况下比较字符，比后面大的替换
            _dict[i],_dict[i+1] = _dict[i+1],_dict[i]
print "更改过的list"
print _dict[:10]


'''
不错
使用dict对字符串中的字符计数
使用setdefault初始化字符个数
使用冒泡排序对每个元素的都是tuple的list进行从大到小排序，并对元素tuple中的多项比较，
使用切片获取排序后列表的前十位

继续加油

'''