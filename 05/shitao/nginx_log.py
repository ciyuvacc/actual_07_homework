#/usr/bin/env python
#coding=utf-8
#file_name = "www_access_20140823.log"
def nginx_log(file_name):
	dict_list = {}
	try:
		# 把日志从文件中读取出来以字典的形式储存 便于后面处理
		_file = open(file_name,'r')
		#_file2 = open('test.txt','a')
		for line in _file.readlines():
			new_line = line.split()
			ip = new_line[0]			# 获取url里面的ip
			status = new_line[8]		# 获取url里面的状态
			url = new_line[6]			# 获取url里面的地址
			dict_list.setdefault((status,url,ip),0)
			dict_list[(status,url,ip)] += 1
		_file.close()
		return dict_list
	except BaseException:
		print "There have been some mistake maybe the %s is not exist " % file_name

def cmp_list(e1,e2):
	return e1 > e2

def list_sort(dict_list):
	# 比较大小 列出排名前十的日志 并按指定格式展示
 	_dict = dict_list.items()
	if len(_dict) -1 > 10:
		sort_len = 10
	for j in range(sort_len):
		for i in range(len(_dict) -1):
			if cmp_list(_dict[i][1],_dict[i+1][1]):
				_dict[i],_dict[i+1] = _dict[i+1],_dict[i]
		res = _dict[(j+1)*-1]
		_list = [res[0][0],res[0][1],(res[0][-1],res[-1])]
		print _list


if __name__ == '__main__':
	dict_list = nginx_log('www_access_20140823.log')
	list_sort(dict_list)
