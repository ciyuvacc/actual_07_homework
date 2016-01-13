#!/usr/bin/env python
#coding=utf-8
# sorted and lamdba
# Level 1
def _sorted(_list,reverse=False):
	_result = sorted(_list,key=lambda _list:max(_list),reverse=reverse)
	print "the result is %s" %_result
_sorted([(1,4),(5,1),(2,3)])

# Level 2
def _sorted2(_list,reverse=False):
	_result = sorted(_list,key=lambda _list:(_list[0] if _list[0]>_list[1] else _list[1]),reverse=reverse)
	#_result = sorted(_list,key=lambda _list:(_list[0]>_list[1] and _list[0] or _list[1]),reverse=reverse)
	print "the result is %s" %_result
_sorted2([(1,4),(5,1),(2,3)])

