#coding=utf-8
'''
流程:
1. 从seq索引为1的元素从左到右遍历
2. 依次比较当前遍历元素前的元素，如果比当前元素大，则向后移动，并记录当前位置，知道无元素比较时结束比较，并将遍历元素插入当比较元素位置后或list头
3. 重复1, 2步骤

评注:
1. 排序结果正确
2. 定义函数的方式实现功能, 并对列表进行相应检查，使用异常处理
3. 借助tmp, pos变量使用的插入排序算法

改进:
1. python中结尾;可以省略

加油
'''

seq = [91,4,2,1,5,11,7,10,22,33,55]

for i in range(1,len(seq)):
        tmp=seq[i]
        pos=i
        for j in range(i-1,-1,-1):
            if seq[j]>tmp:
                seq[j+1]=seq[j]
                pos=j
        seq[pos]=tmp
print '排序结果:%s' %seq #排序结果



num_list = [91,4,2,1,5,11,7,10,22,33,55]

start = 9
end = -1
step = -1

for idx in range(start,end,step):
    if num_list[idx] < num_list[idx-1]:
        num_list[idx],num_list[idx-1] = num_list[idx-1],num_list[idx]
    else:
        break
print num_list








