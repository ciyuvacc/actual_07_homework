#!/usr/bin/env python
#encoding: utf-8
read_me = '''
first of all, i want make it clear that i can not claim understanding this holy book  in just a few weeks, and i would not dare comment on this sacred book, in addition, i don't think i can give you a full picture of the holy bible in just few words.i can not preach anything here. what i want to do here is to express my understanding by sharing two events described in this book. the fist story i want to share is abandoned tower of babel.according to the bibel,people use the same language to communicate with each other in ancient times.with the soaring vanity,they decided to build a heaven-reaching tower to show off their achievement, god knows, he change the human language into different kinds and make it difficult for people to communicate with each other,hence the failure of building tower of  babel.this story tells people,never do things in selfishness, but make a life out of enternal glory.the other story,before jesus christ was crucified,he said, father,forgive them, for they know not what they do. with great love, he shouldered all the sins of  people. what can we learn from this story?we live in this world thanks to the love of god, for this reanson, we should make our lives glorious to honor our god.finally,i want to sum up by saying that only if we put our lives in the eternal love of god,can we live a perfect life, and  what you appealed is what god expected!
'''
print '#############################   方法一 #########################################'
# 第一步:统计每个字符的个数并放在字典里面

user_dict = {}
for i in read_me:
	user_dict.setdefault(i, 0)
	user_dict[i] += 1 
print user_dict

#第二步：将字典转换成list并按照由大到小的顺序排序

arr = user_dict.items()
for i in range(1,len(arr)):
	tmp_str = arr[i]
	j= i - 1
	while j >= 0:
		if arr[j][1] < tmp_str[1]:
			arr[j+1] = arr[j]
			arr[j] = tmp_str
		elif arr[j][1] == arr[j+1][1] and arr[j][0] > arr[j+1][0] :
				arr[j], arr[j+1] = arr[j+1], arr[j]
		j -= 1 
print arr



#第三步：取出 list中前10项并添加到字典中


len_arr = len(arr)
if len_arr > 10:
	len_arr = 10
tmp_dict = {}

tmp_dict = dict(arr[0:len_arr])
print tmp_dict




print '#############################   方法二 #########################################'



# 第一步:统计每个字符的个数并放在字典里面

user_dict = {}
for i in read_me:
	user_dict.setdefault(i, 0)
	user_dict[i] += 1 
print user_dict

#第二步： 做颠倒
tmp_dict = {}
for _key, _value in user_dict.items():
	tmp_dict.setdefault(_value, [])
	tmp_dict[_value].append(_key)
print tmp_dict

num_list = tmp_dict.keys()
num_list.sort(reverse=True)
print num_list

_count = 0 
total = 10 
tmp1_dict = {}
for i in num_list:
	_chars = tmp_dict[i]
	_chars.sort()
	for x in _chars:
#		tmp1_dict.setdefault(i, [])
#		tmp1_dict[i].append(x)
		tmp1_dict[x]=i
		_count += 1
		if _count >= total:
			break 
	if _count >= total:
		break
print tmp1_dict

