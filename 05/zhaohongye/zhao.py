#coding:utf-8
import sys
def Log_fenxi(log_name):
    try:
        log_file = open(log_name)
    except IOError:
        print "\n\tNo such file or directory: '%s'" % log_name
        exit()
    log_stat_dict = {}
    global log_stat_list
    log_stat_list = []
    for _line in log_file:
        _line_nodes = _line.split()
        _ip,_url,_code = _line_nodes[0],_line_nodes[6],_line_nodes[8]
        _key = (_ip,_url,_code)
        log_stat_dict.setdefault(_key,0)
        log_stat_dict[_key] += 1
    log_file.close()
    for _key,_value in log_stat_dict.items():
        _ip,_url,_code = _key
        log_stat_list.append([_code,(_ip,_value),_url])
def top_sort(n):
    for j in range(n):
        for i in range(len(log_stat_list) - 1):
            if log_stat_list[i][1][1] > log_stat_list[i+1][1][1]:
                log_stat_list[i],log_stat_list[i+1] = log_stat_list[i+1],log_stat_list[i]
    for top in log_stat_list[:-(n+1):-1]:
        print top
top_n = int(sys.argv[1])
filename = sys.argv[2]
Log_fenxi(filename)
print "========== 访问排行 %s ：状态，IP，访问次数，URL ==========" % top_n
print "\nUsage: %s <Number> <File name>" % sys.argv[0]





'''
ok 非常棒. 文件和topn通过调用参数传递
但是需要注意
line8 应该为sys.exit
line10 慎用global，若需要使用尽量定义在函数外

'''