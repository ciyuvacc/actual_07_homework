handle = open('www_access_20140023.log')

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

for j in range(10):
    for i in range(len(log_list) - 1):
        if log_list[i][2]][1] > log_list[i + 1][2][1]:
            log_list[i],log_list[i+1] = log_list[i+1],log_list[i]

for n in log_list[:-11:-1]:
    print n
