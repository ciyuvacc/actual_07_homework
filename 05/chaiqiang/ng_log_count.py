#coding:utf-8
def ng_count(path):
    _dict = {}
    count_list = []
    ng_file = open(path,'r')

    for line in ng_file:
        ip = line.split(' ')[0]
        url = line.split(' ')[6]
	state= line.split(' ')[8]
	key = (state,url,ip)
	_dict.setdefault(key,0)
	_dict[key]+=1

    ng_file.close()

    for _key,_value in _dict.items():
	_list = list(_key)
	_list.append(_value)
	count_list.append([_list[0],_list[1],(_list[2],_list[3])])
	# print count_list

    for i in range(10):
	for j in range(len(count_list)-1-i):
	    if count_list[j][2][1] > count_list[j+1][2][1]:
            count_list[j],count_list[j+1] = count_list[j+1],count_list[j]

    for i in count_list[:-11:-1]:
        print i

ng_count('/Users/it1/Desktop/python/nginx_log.txt')


'''
ok,  没有问题
注意缩进, 如果我有时候想要获取TOP 10， 有时候想要获取Top 20，应该怎么做呢？
'''
