#!/usr/bin/env python
#-.- coding: utf-8 -.-

import sys

class doHomework(object):
    """This module is used to day 5 homework"""
    def __init__(self, logfile):
        self._logfile = logfile
    
    @staticmethod
    def sorted_list_one(templist):
        """Task 1-level1: use the function 'max'"""
        try:
            newlist = sorted(templist, key=lambda x: max(x))
            return newlist
        except TypeError, e:
            return u'参数必须是迭代对象,请检查！'
        

    @staticmethod
    def sorted_list_two(templist):
        """Task 1-level2: use three item operation"""
        try:
            newlist = sorted(templist, key=lambda x: x[0] > x[1] and x[0] or x[1])
            return newlist
        except IndexError:
            return u'参数必须是迭代对象，且对象中的每个元素是至少有两个元素的迭代对象！'

    def log_analyse(self):
        """Task 2: analyse log by a function"""
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
    
    @staticmethod
    def operate_one(tempstr):
        """Task 3-level1: do not support priority"""
        result = ''
        try:
            for num in tempstr:
                result += num
                if num.isdigit():
                    result = str(eval(result))
            return result
        except SyntaxError:
            return u'SyntaxError: the parameter must be a string type, and element in string must be number or operator'
    
    @staticmethod
    def operate_two(tempstr):
        """Task 3-level1: do not support priority"""
        try:
            return eval(tempstr)
        except SyntaxError:
            return u'SyntaxError: the parameter must be a string type, and element in string must be number or operator'
    


if __name__ == '__main__':
   
    templist = [(1,4), (5,1), (2,3)]
    logfile = '/tmp/www_access_20140823.log'
    tempstr = '1+2+3*5'
    
    #作业1-1：使用max函数排序
    print doHomework.sorted_list_one(templist)
    
    #作业1-2：不使用max函数排序
    print doHomework.sorted_list_two(templist)

    #作业2：分析日志
    analyselog = doHomework(logfile)
    print(analyselog.log_analyse()[:11]) 
    
    #作业3-1：四则运算,不支持优先级
    print doHomework.operate_one(tempstr)

    #作业3-2：四则运算,支持优先级
    print doHomework.operate_two(tempstr)


'''
不错，已经预习了后面类的相关知识
对于排序可以考虑下cmp方式，毕竟使用key只能按照一个值进行排序，如果多个最大值相同时，这时候按第二个最大值进行排序用key是做不到的

表达式使用eval函数没有问题，但是可以自己解析下表达式，主要为练习列表的pop和append（堆的功能）
'''