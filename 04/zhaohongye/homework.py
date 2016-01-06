#coding:utf-8
############ 第一种
f = open('www_access_20140823.log', 'r')
# f = open('1.log', 'r')
_dir = {}
_list = [] 
# 1、统计访问次数（注意同一个IP，可能访问不同的url以及htpp状态） 
##定义字典_dir{(访问状态，访问http，访问IP)，访问次数}
for _line in f.readlines():
	access_ip = _line.split()[0]
	access_state = _line.split()[8]
	access_url = _line.split()[6]
	tmp_list = [access_state,access_url,access_ip]
	_key = tuple(tmp_list)
	_dir.setdefault(_key,1)
	if tmp_list in _list:
		_dir[_key] += 1
	else:
		_list.append(tmp_list)
#2、根据题意，输出结果
a_list = []
for i in _dir.items():
	list1 = [i[0][0],i[0][1],tuple([i[0][2],i[1]])]
	a_list.append(list1)
#3、根据访问次数，排序
for j in range(len(a_list)-1):
	for i in range(len(a_list)-1-j):
		if a_list[i][2][1] < a_list[i+1][2][1]:
			a_list[i],a_list[i+1] = a_list[i+1],a_list[i]
print a_list[:10]

############# 第二种
stat_dict = {}
f = open('www_access_20140823.log', 'r')
#1、找到次数，字典中key为ip,url,code的组合，value为次数
for line in f:
	line_list = line.split()
	ip = line_list[0]
	url = line_list[6]
	code = line_list[8]
	key = (ip,url,code)
	if key not in stat_dict:
		stat_dict[key] = 1
	else:
		stat_dict[key] += 1
f.close()
#2、反转key和value，新的字段key为次数，value为输出结果：[code,url,(ip,value)]
stat_count_dict = {}
for key,value in stat_dict.items():
	new_key = value
	ip,url,code = key
	new_value = [code,url,(ip,value)]
	if new_key not in stat_count_dict:
		stat_count_dict[new_key] = []
	stat_count_dict[new_key].append(new_value)
#3、将次数（key）冒泡排序。
count_list = stat_count_dict.keys()
for j in range(len(count_list) - 1):
	for i in range(len(count_list) - 1):
		if count_list[i] < count_list[i+1]:
			count_list[i],count_list[i+1] = count_list[i+1],count_list[i]
#4、将结果输入到文件
handle = open('rs.txt','w')
for count in count_list:
	for item in stat_count_dict[count]:
		handle.write(str(item) + '\n')
handle.close



'''
不错，使用多种方法练习，最后将结果写入文件，结果正确，很努力，给你点个赞，继续加油

需要注意：
1. 函数的调用一定要用函数名+()，如果不加括号，函数是不调用的，本周咱们回学习函数

'''