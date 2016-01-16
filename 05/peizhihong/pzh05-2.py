# coding:utf-8

# pzh05-2.py

# 作业2:优化log分析

from collections import Counter

# 分析日志，得到信息元组
def infoBuild(fileSource):
	infoLst = []
	with open(fileSource, 'r') as f:
		content = f.xreadlines()
		for line in content:
			lineLst = line.strip().split(' ')
			ip = lineLst[0]
			status = lineLst[8]
			url = lineLst[6]
			infoLst.append((ip,status,url))
	return infoLst

# 分析信息元组的次数
def lstSort(infoLst):
	resLst = []
	resDict = Counter(infoLst)
	for k,v in resDict.iteritems():
		resLst.append([k[1],k[2],(k[0],v)])
	return resLst

def main():
	fileSource = './www_access_20140823.log'
	infoLst = infoBuild(fileSource)
	resLst = lstSort(infoLst)
	for i in resLst:
		print i

if __name__ == '__main__':
	main()



'''
ok没有问题，对不同位置的功能进行抽象，提取并定义多个函数，加油
'''