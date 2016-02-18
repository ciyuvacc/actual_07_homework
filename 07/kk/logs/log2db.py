#encoding: utf-8

import dbutil


'''
DROP TABLE IF EXISTS `webaccess`;
CREATE TABLE `webaccess` (
    `url` text,
    `code` int,
    `ip` varchar(128),
    `cnt` bigint
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
'''

SQL_INSERT = 'INSERT INTO webaccess(ip, url, code, cnt) VALUES(%s, %s, %s, %s);'

# path = 'www_access_20140823.log'
# 将读取log文件封装成函数
# @param str path log文件路径
# @param dict 日志中按照ip url code统计的次数
def read_log(path):
    stat_dict = {}

    handle = open(path, 'r')
    for line in handle:
        line_list = line.split(' ')
        ip = line_list[0]
        url = line_list[6]
        code = line_list[8]

        key = (ip, url, code)
        if key not in stat_dict:
            stat_dict[key] = 1
        else:
            stat_dict[key] = stat_dict[key] + 1

    handle.close()
    return stat_dict

def store2db(stat_dict, n=-1): 
    args_list = []
    for key, value in stat_dict.items():
        ip, url, code = key
        args_list.append((ip, url, code, value))
    return dbutil.bulk_execute_sql(SQL_INSERT, args_list)

if __name__ == '__main__':
    stat_dict = read_log('www_access_20140823.log')
    print store2db(stat_dict)    