#coding:utf-8

num_list =[(1,4),(5,1),(2,3)]

#1
print sorted(num_list,key=lambda n:max(n))

#2
def max_num(a):
    return  a[0] if a[0]>a[1] else a[1]

print sorted(num_list,key=lambda n:max_num(n))
