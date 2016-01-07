#!/usr/bin/env python
#_*_encoding:utf-8:_*_
#支持中文字符输入

#exp2 统计每个字符出现的次数并将次数前十的打印出来。
user_dict={}
count= 0
new_dict={}
list1=[]
read_me ='''first of all, i want make it clear that i can not claim understanding this holy book  in just a few weeks, and i would not dare comment on this sacred book, in addition, i don't think i can give you a full picture of the holy bible in just few words.i can not preach anything here. what i want to do here is to express my understanding by sharing two events described in this book. the fist story i want to share is abandoned tower of babel.according to the bibel,people use the same language to communicate with each other in ancient times.with the soaring vanity,they decided to build a heaven-reaching tower to show off their achievement, god knows, he change the human language into different kinds and make it difficult for people to communicate with each other,hence the failure of building tower of  babel.this story tells people,never do things in selfishness, but make a life out of enternal glory.the other story,before jesus christ was crucified,he said, father,forgive them, for they know not what they do. with great love, he shouldered all the sins of  people. what can we learn from this story?we live in this world thanks to the love of god, for this reanson, we should make our lives glorious to honor our god.finally,i want to sum up by saying that only if we put our lives in the eternal love of god,can we live a perfect life, and  what you appealed is what god expected!
'''

# 先统计个个字符出现的个数
for i in read_me:
	if  i  in user_dict:
		user_dict[i] +=1
	else:
		user_dict[i] = 1
#反转字典
for key,value in user_dict.items():
        if value in new_dict:
                _new_value =new_dict.get(value)
                if type([]) == type(_new_value):
                        new_dict[value].append(key)
                else:
                        new_dict[value]= [_new_value,key]
        else:
                new_dict[value]= key
        count +=1
#反转后的keys导入新的列表，并排序取前十的数值
for a,b in new_dict.items():
        list1.append(a)
list1.sort()
list1.reverse()
c= list1[0:10]
for i in c:
	for k,v in user_dict.items():
		if  i == v:
			print k,v


'''
想法是对的，但是考虑一下，如果read_me中有26个字符，且都出现一次，是将这26个字符都打印出来呢？可以怎么改进下

1. 注意文件中的缩进方式使用4个空格，尽量不要使用tab键，可能导致在不同的编辑器中看到的缩进不一致，导致脚本不能运行

'''