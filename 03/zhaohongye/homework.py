#coding:utf-8
##字符出现次数，筛选top10
read_me = '''
first of all, i want make it clear that i can not claim understanding this holy book  in just a few weeks, and i would not dare comment on this sacred book, in addition, i don't think i can give you a full picture of the holy bible in just few words.i can not preach anything here. what i want to do here is to express my understanding by sharing two events described in this book. the fist story i want to share is abandoned tower of babel.according to the bibel,people use the same language to communicate with each other in ancient times.with the soaring vanity,they decided to build a heaven-reaching tower to show off their achievement, god knows, he change the human language into different kinds and make it difficult for people to communicate with each other,hence the failure of building tower of  babel.this story tells people,never do things in selfishness, but make a life out of enternal glory.the other story,before jesus christ was crucified,he said, father,forgive them, for they know not what they do. with great love, he shouldered all the sins of  people. what can we learn from this story?we live in this world thanks to the love of god, for this reanson, we should make our lives glorious to honor our god.finally,i want to sum up by saying that only if we put our lives in the eternal love of god,can we live a perfect life, and  what you appealed is what god expected!
'''
_dict = {}
for _key in read_me:
	_dict.setdefault(_key,0)
	_dict[_key] += 1
# _list = _dict.items()
# print '_list列表为：'
# print _list
# list_cout = len(_list) - 1
# if list_cout > 10:
# 	list_cout = 10
# print '列表长度为：'
# print list_cout
# for j in range(list_cout):
# 	for i in range(len(_list)-1 -j):
# 		if _list[i][1] > _list[i+1][1]:
# 			_list[i],_list[i+1] = _list[i+1],_list[i]
# 		elif _list[i][1] == _list[i+1][1]:
# 			if _list[i][0] > _list[i+1][0]:
# 				_list[i],_list[i+1] = _list[i+1],_list[i]
# print '排序后的list：'
# print _list
# print _list[-1:-11:-1]

###第二种方法
#统计出现次数对应的字符
num_stat_dict = {}
for _key,_value in _dict.items():
	num_stat_dict.setdefault(_value,[])
	num_stat_dict[_value].append(_key)
print '出现次数对应的字符'
print num_stat_dict
#第三步：对所有出现次数进行排序
num_list = num_stat_dict.keys()
print '所有次数'
print num_list
num_list.sort(reverse=True)
print '排序后'
print num_list
print_cnt = 0
print_total = 15
for num in num_list:
	_chars = num_stat_dict[num]
	_chars.sort()
	for _char in _chars:
		print '字符：%s，出现次数为：%d' % (_char,num)
		print_cnt += 1
		if print_cnt >+ print_total:
			break
	if print_cnt >+ print_total:
			break


'''
不错，思路很清晰，尝试使用不同的方法，结果正确，继续努力


'''
