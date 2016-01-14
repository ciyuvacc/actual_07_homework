#coding=utf-8
#排序
_list = [(1,4), (5,1), (2,3)]
print sorted(_list, key=lambda x: max(x))
print sorted(_list, key=lambda x: x[0] > x[1] and x[0] or x[1])

#分析日志
def alyze_log(logfile):
        log_dict = {}
        log_list = []
        with open(logfile) as f:
            for line in f:
                _line = line.split()
                ip=_line[0]
                url=_line[6]
                code=_line[8]
                log_dict[(code,url,ip)] = log_dict.get((code,url,ip),0)+1


        for key, value in log_dict.iteritems():
            log_list.append([key[0], key[1], (key[2], value)])

        print   sorted(log_list, key=lambda x: x[2][1], reverse=True)[:10]


alyze_log("D:\www_access_20140823.log")

