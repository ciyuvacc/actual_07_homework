#coding=utf-8
#作业：LIST最大的2个值
str1_list = [1,1,65543,3,21,1111,99999,166667,68555,45,33,45]

#第一种排序
str1_list.sort(reverse=True)
print str1_list[0:2]


#第二种
#先找最大的数字，过滤这个最大的，然后在找最大的则而第二大
str2_list = [1,1,65543,3,21,1111,99999,166667,68555,45,33,45]
max_1 = 0
for i in str2_list:
    if i > max_1:
        max_1 = i
max_2 = 0
for i in str2_list:
    if i == max_1:
        continue
    if i > max_2:
        max_2 = i

print max_1,max_2


#第三种
#
str3_list = [1,2,65543,3,21,1111,99999,166667,68555,45,33,45]
max_1=0
max_2=0
if str3_list[0]>str3_list[1]:
    max_1=str3_list[0]
    max_2=str3_list[1]
else:
    max_1=str3_list[1]
    max_2=str3_list[0]

for i in range(2,len(str3_list)):
    if  max_1 < str3_list[i]:
        max_2 = max_1
        max_1 = str3_list[i]
    elif max_2 < str3_list[i]:
        max_2 = str3_list[i]

print max_1,max_2








