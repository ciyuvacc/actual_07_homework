# encoding: utf-8
l = [(1,4),(5,1),(2,3)]

# 列表中的每个元素分别赋值给变量t，用max()函数求出t中最大值赋值给key，并以key做排序生成一个新列表
print sorted(l, key=lambda t: max(t))

# 列表中的每个元素分别赋值给变量t，判断t[0]>t[1]，如果为真，key的值为t[0]；如果为假，key的值为t[1]，最后以key做排序生成一个新列表
print sorted(l, key=lambda t: t[0] if t[0]>t[1] else t[1])
