#coding=utf-8
#排序
_list = [(1,4), (5,1), (2,3)]
print sorted(_list, key=lambda x: max(x))
print sorted(_list, key=lambda x: x[0] > x[1] and x[0] or x[1])

#分析日志
import  sys
def alyze_log(logfile):
        log_dict = {}
        log_list = []
        try:
            with open(logfile) as f:
                for line in f:
                    _line = line.split()
                    ip=_line[0]
                    url=_line[6]
                    code=_line[8]
                    log_dict[(code,url,ip)] = log_dict.get((code,url,ip),0)+1
            log_list = [[key[0], key[1], (key[2], value)] for key,value in log_dict.iteritems()]
        except IOError:
                print 'not found %s' %logfile
                sys.exit()
        return   sorted(log_list, key=lambda x: x[2][1], reverse=True)[:10]

print alyze_log("D:\www_access_20140823.log")



'''
排序功能没有问题

可以试试cmp参数
sorted(num_list, cmp=lambda x, y: 1 if max(x) > max(y) else (0 if max(x) > max(y) else -1))

对于log分析的
如果我有时候想要获取TOP 10， 有时候想要获取Top 20，应该怎么做呢？能不能把它拽变成参数，而且有默认值为10

'''