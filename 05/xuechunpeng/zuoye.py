#encoding: utf-8

#作业1：排序

_list = [(1,4),(5,1),(2,3)]
#方法一：列表中的每个元素分别赋值给变量x，用max()函数求出x中最大值赋值给key，并以key做排序生成一个新列表
print sorted(_list, key = lambda x: max(x))
#方法二：
print sorted(_list, key = lambda x: x[0]>x[1] and x[0] or x[1])

#作业2：日志分析

def log_fenxi(log_name)

handle = open(log_name)
while True:
    _line = handle.readline() #读取一行
    #判断文件是否已经读完
    if '' = _line:
        break
    #解析每一行
    _logs = _line.split()
    _ip = _logs[0]
    _url = _logs[6]
    _code = _logs[8]

    _key = (_ip, _url, _code)
    log_dict.setdefault(_key,0)
    log_dict[_key] +=1

handle.close()

#dict=>list

log_list = []
for _key in log_dict:
    _value = log_dict[_key]
    _ip,_url,_code = _key
    log_list.append([_code,_url,(_ip,_value)])

def top_sort(n)

for j in range(n):
    for i in range(len(log_list) - 1):
        if log_list[i][2]][1] > log_list[i + 1][2][1]:
            log_list[i],log_list[i+1] = log_list[i+1],log_list[i]

for t in log_list[:-(n+1):-1]:
    print t

