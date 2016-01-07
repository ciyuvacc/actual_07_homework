#!/usr/bin/env python
#-*- coding: utf-8 -*-

import sys

class AnalyseLog(object):
    """This class be used for analyse nginx log"""
    def __init__(self, logfile):
        self._logfile = logfile

    def main(self):
        total_stat = {}
        result = []
        try:
            with open(self._logfile) as f:
                for line in f:
                    statlist = line.split()
                    total_stat.setdefault((statlist[8], statlist[6], statlist[0]), 0)
                    total_stat[(statlist[8], statlist[6], statlist[0])] += 1
        except IOError:
            print('The log file named \033[1;32m"%s"\033[0m is not exist, please check again!' % self._logfile)
            sys.exit(1)

        for key, value in total_stat.iteritems():
            result.append([key[0], key[1], (key[2], value)])

        return sorted(result, key=lambda x: x[2][1], reverse=True)


if __name__ == '__main__':
    
    logfile = '/tmp/www_access_20140823.lo'
    analyselog = AnalyseLog(logfile)
    print(analyselog.main()[:11])


'''
不错，预习了函数，类，with等知识，结果正确

继续加油

'''