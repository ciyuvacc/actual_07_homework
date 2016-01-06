
#coding=utf-8
#试写 第一版本
#coding=utf-8

def read_file():
            log_dict = {}
            res_dict = []
            f=open("www_access_20140823.log", "r")
            contents = f.readlines()
            f.close()
            for line in contents:
                log_ip=line.split()[0]
                log_url=line.split()[6]
                log_code=line.split()[8]
                log_dict[(log_ip,log_url,log_code)]=log_dict.setdefault((log_ip,log_url,log_code), 0) +1

            for k,v in log_dict.iteritems():
                res_dict.append([k[2], k[1], (k[0], v)])

            for l in sorted(res_dict, key=lambda x:x[2][1], reverse=True)[:10]:
                 print l
read_file()





'''
不错已经预习了函数的知识，结果正确
可以改进的地方：
1. 13,14,15使用3次split，可否改成一个？
2. 注意缩进

'''