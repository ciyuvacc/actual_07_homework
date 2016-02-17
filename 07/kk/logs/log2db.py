#encoding: utf-8

import MySQLdb

DB_HOST = 'localhost'
DB_PORT = 3306
DB_USER = 'root'
DB_PASSWD = '881019'
DB_NAME = 'test'
DB_CHARSET = 'utf8'


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
    _conn, _cur = None, None
    _rt_cnt = 0
    try:
        # 步骤1
        _conn = MySQLdb.connect(host=DB_HOST, port=DB_PORT, \
                                user=DB_USER, passwd=DB_PASSWD, \
                                db=DB_NAME, charset=DB_CHARSET)

        _cur =_conn.cursor() 
        for key, value in stat_dict.items():
            ip, url, code = key
            _rt_cnt += _cur.execute(SQL_INSERT, (ip, url, code, value))
        _conn.commit()
    except BaseException, e:
        print str(e)                                        # 打印异常
    finally:
        if _cur is not None:
            _cur.close()
        if _conn is not None:
            _conn.close()
    return _rt_cnt

if __name__ == '__main__':
    stat_dict = read_log('www_access_20140823.log')
    print store2db(stat_dict)    