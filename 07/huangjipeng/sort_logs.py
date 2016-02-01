#!/usr/bin/env python
#zuoye1
import time
from models import mysql_conn
import gconf

def _get_max(x):
    return x[0] if x[0] > x[1] else x[1]
def _cmp_element(x1,x2):
    max_x1 = _get_max(x1)
    max_x2 = _get_max(x2)
    return max_x1 > max_x2

def log_count_dict(log_path):
    log_dict = {}
    log_file = open(log_path,'r')
    for file_line in log_file:
        line_list = file_line.split(' ')
        try:
            _ip = line_list[0]
            _url = line_list[6]
            _code = line_list[8]
            _key = (_ip,_url,_code)
            log_dict.setdefault(_key,0)
            log_dict[_key] += 1
        except BaseException as e:
            with open('error.log','a') as fd:
                print >> fd,e
            continue
    log_file.close()
    return log_dict
def log_list(log_dict,n):
    log_list = []
    for _key in log_dict:
        _ip,_url,_code = _key
        _value = log_dict[_key]
        log_list.append([_code,_url,(_ip,_value)])
    new_log_list = sorted(log_list,reverse=True,key=lambda x:x[2][1])
    #return new_log_list[:n-1]
    return new_log_list

def log_write(sort_list):
    conn = mysql_conn()
    cur = conn.cursor()
    for s in sort_list:
        print s
        cur.execute('INSERT INTO logs(ip, url, code,count) VALUES(%s, %s, %s, %s) ', \
                                           (s[2][0], s[1], s[0], s[2][1]))
    conn.commit()
    cur.close()
    conn.close()
def log_print(sort_list):
    for x in sort_list:
       print x     
def run(file_log='/root/cmdb/access.log',n=10):
    log_dict = log_count_dict(file_log)
    sort_list = log_list(log_dict,n)
    log_write(sort_list)
if __name__ == "__main__":
    run()

