#!/usr/bin/python
#coding:utf-8
read_me = '''
first of all, i want make it clear that i can not claim understanding this holy book  in just a few weeks, and i would not dare comment on this sacred book, in addition, i don't think i can give you a full picture of the holy bible in just few words.i can not preach anything here. what i want to do here is to express my understanding by sharing two events described in this book. the fist story i want to share is abandoned tower of babel.according to the bibel,people use the same language to communicate with each other in ancient times.with the soaring vanity,they decided to build a heaven-reaching tower to show off their achievement, god knows, he change the human language into different kinds and make it difficult for people to communicate with each other,hence the failure of building tower of  babel.this story tells people,never do things in selfishness, but make a life out of enternal glory.the other story,before jesus christ was crucified,he said, father,forgive them, for they know not what they do. with great love, he shouldered all the sins of  people. what can we learn from this story?we live in this world thanks to the love of god, for this reanson, we should make our lives glorious to honor our god.finally,i want to sum up by saying that only if we put our lives in the eternal love of god,can we live a perfect life, and  what you appealed is what god expected!
'''
#方法一
read_me = 'abcdefghi'
#第一步：统计每一个字符出现的次数
_dict = {}
for i in read_me:
    _dict.setdefault(i,0)
    _dict[i] = _dict[i] + 1
print _dict 

#第二步：由于dict无序的无法排序，故将dict转化为list
_list = _dict.items() 

#排序
_count = len(_list) - 1
if _count > 10:
    _count = 10
 
for k in range(_count):
    for i in range(_count - k ):
        if _list[i][1] > _list[i + 1][1]:
	    tmp = _list[i]
	    _list[i] = _list[i + 1]
	    _list[i + 1] = tmp
        elif _list[i][1] == _list[i + 1][1]:
	    if _list[i][0] < _list[i + 1][0]:
		tmp = _list[i]
                _list[i] = _list[i + 1]
                _list[i + 1] = tmp
print _list
#切片
print _list[-1:-11:-1]
for i in _list[-1:-11:-1]:
    print '字符为%s的出现次数为%d' %i
#pop弹出
#for i in range(10):
#    print _list.pop()	
#方法二：
read_me = '''
first of all, i want make it clear that i can not claim understanding this holy book  in just a few weeks, and i would not dare comment on this sacred book, in addition, i don't think i can give you a full picture of the holy bible in just few words.i can not preach anything here. what i want to do here is to express my understanding by sharing two events described in this book. the fist story i want to share is abandoned tower of babel.according to the bibel,people use the same language to communicate with each other in ancient times.with the soaring vanity,they decided to build a heaven-reaching tower to show off their achievement, god knows, he change the human language into different kinds and make it difficult for people to communicate with each other,hence the failure of building tower of  babel.this story tells people,never do things in selfishness, but make a life out of enternal glory.the other story,before jesus christ was crucified,he said, father,forgive them, for they know not what they do. with great love, he shouldered all the sins of  people. what can we learn from this story?we live in this world thanks to the love of god, for this reanson, we should make our lives glorious to honor our god.finally,i want to sum up by saying that only if we put our lives in the eternal love of god,can we live a perfect life, and  what you appealed is what god expected!
'''
read_me = 'abcdefghi'
#第一步：统计每一个字符出现的次数
_dict = {}
for i in read_me:
    _dict.setdefault(i,0)
    _dict[i] = _dict[i] + 1
print _dict

#第二步：统计出现次数的字符
num_stat_dict = {}

for _key,_value in _dict.items():
    num_stat_dict.setdefault(_value,[])
    num_stat_dict[_value].append(_key)

print '出现次数对应的字符'
print num_stat_dict

#第三步：对所有出现次数进行排序

_list = num_stat_dict.keys()
print _list
_list.sort(reverse=True)
print _list

_count = 0
for i in _list:
    _chars = num_stat_dict[i]
    _chars.sort()
    print _chars
    for k in _chars:
	print '字符%s出现的次数为%d' %(k,i)
        _count += 1
	if _count == 10:
	    break
    if _count == 10:
	break
 
