# coding:utf-8

# pzh05-1.py

# 作业1:排序

def lstSort(lst):
	# 级别1
	#sortLst = sorted(lst,key = lambda x: max(x[0],x[1]))
	# 级别2
	sortLst = sorted(lst,key = lambda x: (x[0] > x[1] and x[0] or x[1]))
	return sortLst

def main():
	lst = [(8,2),(9,3),(1,4),(5,1),(2,3),(0,-9)]
	print lstSort(lst)

if __name__ == '__main__':
	main()