#encoding: utf-8

read_me = '''
first of all, i want make it clear that i can not claim understanding this holy book  in just a few weeks, and i would not dare comment on this sacred book, in addition, i don't think i can give you a full picture of the holy bible in just few words.i can not preach anything here. what i want to do here is to express my understanding by sharing two events described in this book. the fist story i want to share is abandoned tower of babel.according to the bibel,people use the same language to communicate with each other in ancient times.with the soaring vanity,they decided to build a heaven-reaching tower to show off their achievement, god knows, he change the human language into different kinds and make it difficult for people to communicate with each other,hence the failure of building tower of  babel.this story tells people,never do things in selfishness, but make a life out of enternal glory.the other story,before jesus christ was crucified,he said, father,forgive them, for they know not what they do. with great love, he shouldered all the sins of  people. what can we learn from this story?we live in this world thanks to the love of god, for this reanson, we should make our lives glorious to honor our god.finally,i want to sum up by saying that only if we put our lives in the eternal love of god,can we live a perfect life, and  what you appealed is what god expected!
'''

#read_me = 'nmlkjihgfedcba'

'''
第一步:统计每个字符出现的次数
'''
char_stat_dict = {}
for _char in read_me:
	char_stat_dict.setdefault(_char, 0)
	char_stat_dict[_char] += 1

print '每个字符对应的次数:'
print char_stat_dict

'''
第二步:dict=>list
'''

char_stat_list = char_stat_dict.items()
print '获取dict对应的list'
print char_stat_list

'''
{'a' : 5, 'b' : 10, 'c' : 3}
=>[('a', 15), ('b', 10), ('c', 3)]
要把第一个数量最多的冒泡到最后
for x range(len() - 1):
比较索引为x和x+1
0, (a, 15), (b, 1) => b, a, c
1, (a, 15), (c, 3) => b c a  
2, (c, 3),  


1. [('b', 10), ('c', 3), ('a', 15)]
2. [ ('c', 3), ('b', 10), ('a', 15)]

'''

'''
第三步: list排序, 冒泡
1. tuple可以进行比较的
2. 可以用元组中的某个元素代码元组，和其他元组比较
'''
print '元素个数:%d' %  len(char_stat_list)

sort_cnt = len(char_stat_list) - 1 
if sort_cnt > 10:
    sort_cnt = 10

for j in range(sort_cnt):
	for i in range(len(char_stat_list) - 1 - j): #第N计较，已经排序了N-1(j) 
		if char_stat_list[i][1] > char_stat_list[i + 1][1]:
			#a, b = b, a
			char_stat_list[i], char_stat_list[i + 1] = char_stat_list[i + 1], char_stat_list[i]
                elif char_stat_list[i][1] == char_stat_list[i + 1][1]:
                     if char_stat_list[i][0] < char_stat_list[i + 1][0]:
			char_stat_list[i], char_stat_list[i + 1] = char_stat_list[i + 1], char_stat_list[i]

'''
有序列表, 从小到大
'''
print '排序后的有序列表:'
print char_stat_list

'''
拿出top10
'''
print '排序后的top10'
print char_stat_list[-1:-11:-1]


print '每一个元素'
for x in char_stat_list[-1:-11:-1]:
    print '字符:%s对应次数:%d' % x 
