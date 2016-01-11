# encoding=utf-8
#

read_me = '''
first of all, i want make it clear that i can not claim understanding this holy book in just a few weeks, and i would not dare comment on this sacred book, 
in addition, i don't think i can give you a full picture of the holy bible in just few words.i can not preach anything here. 
what i want to do here is to express my understanding by sharing two events described in this book. 
the fist story i want to share is abandoned tower of babel.according to the bibel,
people use the same language to communicate with each other in ancient times.with the soaring vanity,
they decided to build a heaven-reaching tower to show off their achievement, god knows, 
he change the human language into different kinds and make it difficult for people to communicate with each other,
hence the failure of building tower of babel.this story tells people,never do things in selfishness, 
but make a life out of enternal glory.the other story,before jesus christ was crucified,he said, 
father,forgive them, for they know not what they do. with great love, he shouldered all the sins of people. 
what can we learn from this story?we live in this world thanks to the love of god, for this reanson, 
we should make our lives glorious to honor our god.finally,i want to sum up by saying that only if we put our lives in the eternal love of god,
can we live a perfect life, and what you appealed is what god expected!
'''

# 方法一(有缺陷)
count_dict = {}

for i in read_me:
	count_dict.setdefault(i,0)
	count_dict[i] += 1

#print count_dict

top10_list = []

for _key in count_dict:
	top10_list.append(count_dict[_key])

top10_list.sort()
top10_list.reverse()

top10_list_uniq = []

for i in top10_list:
	if i not in top10_list_uniq:
		top10_list_uniq.append(i)	

top10_list = top10_list_uniq[:10]

#print top10_list

count_dict_top10 = []

for _value in top10_list:
	for j in count_dict:
		if count_dict[j] == _value:
			count_dict_top10.append(j)		

print "Top 10 string and count number are: "
print count_dict_top10[:10]

# 方法二
count_dict = {}

for i in read_me:
	count_dict.setdefault(i,0)
	count_dict[i] += 1

#print count_dict

top10_list = []
top10_list = count_dict.items()

#print top10_list

sort_cnt = len(top10_list) - 1

if sort_cnt > 10:
	sort_cnt = 10

for i in range(sort_cnt):
	for j in range(len(top10_list) - 1 - i):
		if top10_list[j][1] > top10_list[j+1][1]:
			top10_list[j],top10_list[j+1]= top10_list[j+1],top10_list[j]
		elif top10_list[j][1] == top10_list[j+1][1]:
			if top10_list[j][0] < top10_list[j+1][0]:
				top10_list[j],top10_list[j+1]= top10_list[j+1],top10_list[j]

#print top10_list[-1:-11:-1]

print "Top 10 string and count number are: "
for x in top10_list[-1:-11:-1]:
	print "string: \"%s\",count number is: %d" % x

# 方法三
char_stat_dict = {}

for _char in read_me:
	char_stat_dict.setdefault(_char,0)
	char_stat_dict[_char] += 1
#print char_stat_dict

num_stat_dict = {}

for _key,_value in char_stat_dict.items():
	num_stat_dict.setdefault(_value,[])
	num_stat_dict[_value].append(_key)
#print num_stat_dict

num_list = num_stat_dict.keys()
num_list.sort(reverse=True)
#print num_list

print_cnt = 0
print_cnt_total = 10
print "Top 10 string are: "
for num in num_list:
	_chars = num_stat_dict[num]
	_chars.sort()
	for _char in _chars:
		print "String: \"%s\",count number: %d" % (_char,num)
		print_cnt += 1
		if print_cnt >= print_cnt_total:
			break	
	if print_cnt >= print_cnt_total:
		break
