#coding:utf-8

num_list =[(1,4),(5,1),(2,3)]

#1
print sorted(num_list,key=lambda n:max(n))

#2
def max_num(a):
    return  a[0] if a[0]>a[1] else a[1]

print sorted(num_list,key=lambda n:max_num(n))

'''
ok,  没有问题，可以试试
sorted(num_list, key=lambda a: a[0] if a[0]>a[1] else a[1])
另外可以试试cmp参数
sorted(num_list, cmp=lambda x, y: 1 if max_num(x) > max_num(y) else (0 if max_num(x) > max_num(y) else -1))

'''
