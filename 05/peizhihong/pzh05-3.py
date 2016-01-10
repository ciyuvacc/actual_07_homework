# coding:utf-8

# pzh05-3.py

# 作业3：加减乘除

from __future__ import division

def operate(input_str):
	try:
		return eval(input_str)
	except Exception,e:
		return str(e)

def main():
	input_str = raw_input("input expression: ")
	res = operate(input_str)
	if isinstance(res, int):
		print "The '%s' result is: %d" % (input_str, res)
	elif isinstance(res, float):
		print  "The '%s' result is: %f" % (input_str, res)
	else:
		print 'Some thing maybe worng: ' + res

if __name__ == '__main__':
	main()
