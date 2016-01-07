# encoding:utf-8
#读取日志文件并初始化字典内容
with open('access.log', 'r') as log:
    dict = {}
    for line in log:
        line_list = line.split(' ')
        _ip = line_list[0]
        _url = line_list[6]
        _code = line_list[8]
        _lines = (_ip, _url, _code)
        if _lines not in dict:
            dict[_lines] = 1
        else:
            dict[_lines] += 1
#创建第二个字典，内容为未排序的结果
dict_2 = {}
for key, value in dict.items():
    dict_2_key = value
    _ip, _url, _code = key
    dict_2_value = (_code, _url, [_ip, value])
    if dict_2_key not in dict_2:
        dict_2[dict_2_key] = []
    dict_2[dict_2_key].append(dict_2_value)

#对访问结果进行排序
count = dict_2.keys()
for x in range(len(count) - 1):
    for y in range(len(count) - 1):
        if count[y] < count[y + 1]:
            count[y], count[y + 1] = count[y + 1], count[y]

#创建排序后的列表，根据排序结果按从大到小的顺序写入列表
last_text = []
for count_l in count:
    for item in dict_2[count_l]:
        last_text.append(item)

#把最后的列表写入一个文件
with open('test.txt', 'w') as test:
    for x in last_text:
        test.write(str(x) + "\n")
