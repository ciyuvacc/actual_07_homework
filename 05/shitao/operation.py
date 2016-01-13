#!/usr/bin/env python
#coding=utf-8
level = {
	'+':{'lv':1,'ex':lambda x,y:x+y},
	'-':{'lv':1,'ex':lambda x,y:x-y},
	'*':{'lv':2,'ex':lambda x,y:x*y},
	'/':{'lv':2,'ex':lambda x,y:x/y}
} 

'''
 思路：
	把中缀表达式转换成后缀表达式。即 1+2*3-5 => 123*+5-
	在通过lambda来运算这些后缀表达式
'''
# 级别1 不考虑运算符的优先级 即处理完的后缀表达式为 12+3*5-

def priority1(_str):
	# 设置两个列表，存放数字和运算符
	_number = []
	_opera = []
	temp_number = ''
	# 遍历_str 如果是数字就把他放在数字的列表里面，如果是运算符就把他放在另一个列表里面
	for i in _str:
		if i not in level:
			temp_number += i   # 这不是为了处理两位数的数字，
		else:
			_opera.append(i)
			_number.append(temp_number)
			# 判断 当数字列表里面的个数大于等于2的时候吧运算符一次append到数字后面
			if len(_number) >= 2:
				_number.append(_opera.pop(0))
			temp_number = ''
	_number.append(temp_number)
	_number.extend(_opera)
	return _number

# 级别 2 考虑运算符的优先级

def priority2(_str):
	# 设置两个列表，存放数字和运算符
	_opera = []
	_number = []
	temp_number = ''
	# 遍历_str 如果是数字就把他放在数字的列表里面，如果是运算符就把他放在另一个列表里面
	for i in _str:
		if i in level:
			_number.append(temp_number)
			if len(_opera) == 0:
				_opera.append(i)
			elif level[i]['lv'] < level[_opera[-1]]['lv']: # 比较操作符的优先级，如果比栈顶得元素优先级小，把操作符栈全部入栈到数字栈，并且把最新的的这个操作符入栈
				_number.extend(_opera[::-1])
				_opera = [i]                # 如果此操作符的优先级，比操作符栈顶得元素优先级小，把操作符栈全部入栈到数字栈，并且最新的这个操作符入栈
			else:
				_opera.append(i)
			temp_number = ''		# 一组数字成功组合之后，把他的值设置成空，便于下次使用
 		else:
 			temp_number+=i
	_number.append(temp_number)
	_number.extend(_opera[::-1])
	return _number

# 运算操作
# 遍历前面处理好的后缀表达式使其变成想要的格式
def opera(arr):
	temp_list = []
	for i in arr:
		if i not in level:
			# 把数字放到列表中
			temp_list.append(int(i))
		else:
			# 如果是运算符号 取出运算服之前的两个数字
			number1 = temp_list.pop()
			number2 = temp_list.pop()
			result_number = level[i]['ex'](number2,number1)   # 对运算符之前的两个数字进行计算 把结果append到列表处
			temp_list.append(result_number)
	print  temp_list

# 级别1
arr = priority1('1+2*3-5')
# 级别2
arr = priority2('1+2*3-5')
opera(arr)