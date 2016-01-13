#encoding: utf-8
_list = [(1,4),(5,1),(2,3)]

#方法一：列表中的每个元素分别赋值给变量x，用max()函数求出x中最大值赋值给key，并以key做排序生成一个新列表
print sorted(_list, key = lambda x: max(x))

#方法二：
print sorted(_list, key = lambda x: x[0]>x[1] and x[0] or x[1])

