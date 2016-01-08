#!/usr/bin/env python
#coding=utf-8
file_name = "www_access_20140823.log"
_dict = {}
try:
	# 把日志从文件中读取出来以字典的形式储存 便于后面处理
	_file = open(file_name,'r')
	for line in _file:
		full_url = line.split()[8],line.split()[6],line.split()[0]
		_dict.setdefault(full_url,0)
		_dict[full_url] += 1
	_file.close()
except BaseException:
	print "There have been some mistake maybe the %s is not exist " % file_name
else:
	# 比较大小 列出排名前十的日志 并按指定格式展示
 	_dict = _dict.items()
	if len(_dict) -1 > 10:
		sort_len = 10
	for j in range(sort_len):
		for i in range(len(_dict) -1):
			if _dict[i][1] > _dict[i+1][1]:
				_dict[i],_dict[i+1] = _dict[i+1],_dict[i]
		res = _dict[(j+1)*-1]
		_list = [res[0][0],res[0][1],(res[0][-1],res[-1])]
		print _list



'''
不错，结果正确，练习使用文件，异常等知识点

可以改进的地方
1. 9行用了3次split，是否可以改成一个呢，将元组赋值给一个变量建议用()括起来，明确表示其妻一个元组

'''