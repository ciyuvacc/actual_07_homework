#!/usr/bin/env python
#encoding:utf8
read_me = '''
first of all, i want make it clear that i can not claim understanding this holy book  in just a few weeks, and i would not dare comment on this sacred book, in addition, i don't think i can give you a full picture of the holy bible in just few words.i can not preach anything here. what i want to do here is to express my understanding by sharing two events described in this book. the fist story i want to share is abandoned tower of babel.according to the bibel,people use the same language to communicate with each other in ancient times.with the soaring vanity,they decided to build a heaven-reaching tower to show off their achievement, god knows, he change the human language into different kinds and make it difficult for people to communicate with each other,hence the failure of building tower of  babel.this story tells people,never do things in selfishness, but make a life out of enternal glory.the other story,before jesus christ was crucified,he said, father,forgive them, for they know not what they do. with great love, he shouldered all the sins of  people. what can we learn from this story?we live in this world thanks to the love of god, for this reanson, we should make our lives glorious to honor our god.finally,i want to sum up by saying that only if we put our lives in the eternal love of god,can we live a perfect life, and  what you appealed is what god expected!
'''
#遍历一段字符串，计算每个字符串出现的次数，生成一个字典 
_oldlst = {}
for key in read_me:
    #if key in _oldlst:
    if  _oldlst.get(key):
        _oldlst[key] += 1
    else:
        _oldlst[key] = 1


print "方法一：\n\n"


#将字典转为列表，根据索引遍历列表，并对比较两个元素内的次数做比较，插入排序
new_lst = _oldlst.items()
#print new_lst
for i in range(1,len(new_lst)):
    for j in range(i,0,-1):
        #a,b = new_lst[j]
	#c,d = new_lst[j - 1 ]
        #if b < d:
	if (new_lst[j])[1] < (new_lst[j -1])[1]:
            new_lst[j],new_lst[j - 1 ] = new_lst[j - 1 ],new_lst[j]
        else:
            break
#print new_lst[len(new_lst):(len(new_lst)-11):-1]
#在排序后的列表中从后切片出10个元组，打印
for i in new_lst[len(new_lst):(len(new_lst)-11):-1]:
    #a,b = i
    print "出现最多的 '%s'   次数为'%s'"  % i
    #print '出现最多的 %s , 次数为%s'  % (a,b)

print '''

方法二：
'''
# 冒泡排序从大到小排出最大的10个，并循环打印出
for ch in range(10): #要排序的个数
    for x in range(len(new_lst) -1,0,-1):
        if (new_lst[x])[1] > (new_lst[x - 1])[1]:
	    new_lst[x],new_lst[x - 1] = new_lst[x - 1],new_lst[x]
        else:
	    continue
    new_lst2 = new_lst[:ch + 1]
    print  "出现最多的 '%s' , 出现次数为'%s'"  % new_lst2[ch]
	
    

'''
不错，尝试了两种方法排序算法，结果是正确的

1. 注意文件中的缩进方式使用4个空格，尽量不要使用tab键，可能导致在不同的编辑器中看到的索引不一样
2. (new_lst[x])[1] ==> new_lst[x][1]


'''

    
