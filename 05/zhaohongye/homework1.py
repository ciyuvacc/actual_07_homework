#coding:utf-8
#排序（以第二个元素）：
#方法一  sort中以key排序
# list1 = [('a',1),('b',3),('c',2),('d',7)]
# def _key(e):
#     return e[1]
# list1.sort(key=_key)
# print list1

#方法二 sort中已cmp排序
# list1 = [('a',1),('b',3),('c',2),('d',7)]
# def _cmp(e1,e2):
#     return 1 if e1[1] > e2[1] else (0 if e1[1] == e2[1] else -1)
# list1.sort(cmp=_cmp)
# print list1

##作业一
#一个list[(1,4),(5,1),(2,3)],根据每个元组中的较大值进行排序
#1、sort方法
list = [(1,4),(5,1),(90,1),(2,3)]
def a(e):
    return max(e)
list.sort(key=a)
print list
#2、lambda方法
g = lambda x: max(x) 
#3、lambda方法（不用max函数）
g = lambda x: x[0] if x[0]>x[1] else x[1]
for j in range(len(list)-1):
	for i in range(len(list)-1-j):
		if g(list[i]) > g(list[i+1]):
			list[i],list[i+1]=list[i+1],list[i]
print list




