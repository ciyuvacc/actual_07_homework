def split_str(txt):
	node_list = []
	tmp_str = ''
	chs = list('0123456789+-*/.')
	for i in txt:
		if i not in chs:
			continue
		if i in ['+','-','*','/']:
			if tmp_str != '':
				node_list.append(tmp_str)
				tmp_str = ''
			node_list.append(i)
		else:
			tmp_str += i

	if tmp_str != '':
		node_list.append(tmp_str)

	return node_list


def calc1(node_list):
	leftnum = float(node_list[0])
	
	for t in range(1, len(node_list), 2):
		_op = node_list[t]
		rightnum = float(node_list[t+1])
		if _op == '+':
			leftnum += rightnum
		elif _op == '-':
			leftnum -= rightnum
		elif _op == '*':
			leftnum *= rightnum
		elif _op == '/':
			leftnum /= rightnum
	return leftnum

def calc2(node_list):
    num_list = []
    op_list = []
    ops = list('+-*/')
    i = 0
    while i < len(node_list):
        if node_list[i] in ops:
            if len(op_list) == 0:
                op_list.append(node_list[i])
            else:
                if op_list[-1] == '+':
                    if node_list[i] == '+' or node_list[i] == '-':
                        num_right = num_list.pop()
                        num_left = num_list.pop()
                        op_list.pop()
                        num_list.append(float(num_left) + float(num_right))
                        i -= 1
                    else:
                        op_list.append(node_list[i])
                elif op_list[-1] == '-':
                    if node_list[i] == '+' or node_list[i] == '-':
                        num_right = num_list.pop()
                        num_left = num_list.pop()
                        op_list.pop()
                        num_list.append(float(num_left) - float(num_right))
                        i -= 1
                    else:
                        op_list.append(node_list[i])
                elif op_list[-1] == '*':
                    num_right = num_list.pop()
                    num_left = num_list.pop()
                    op_list.pop()
                    num_list.append(float(num_left) * float(num_right))
                    i -= 1
                else:
                    num_right = num_list.pop()
                    num_left = num_list.pop()
                    op_list.pop()
                    num_list.append(float(num_left) / float(num_right))
                    i -= 1
        else:
            num_list.append(node_list[i])
        i += 1

    while len(op_list) > 0:
        num_right = num_list.pop()
        num_left = num_list.pop()
        op = op_list.pop()
        if op == '+':
            num_list.append(float(num_left) + float(num_right))
        elif op == '-':
            num_list.append(float(num_left) - float(num_right))
        elif op == '*':
            num_list.append(float(num_left) * float(num_right))
        elif op == '/':
            num_list.append(float(num_left) / float(num_right))

    return num_list.pop()

d = split_str('1+3*4-5')
print d
print calc1(d)
print calc2(d)
