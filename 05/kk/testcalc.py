#encoding: utf-8


# 将字符串按+, -, *, /, (, )进行切分
def split_str(txt):
    node_list = []
    temp_str = ''
    chs = list('0123456789+-*/.')
    for c in txt:
        if c not in chs: #过滤字符
            continue
        if c in ['+', '-', '*', '/']:
            if temp_str != '':
                node_list.append(temp_str)
                temp_str = ''
            node_list.append(c)
        else:
            temp_str += c
    if temp_str != '':
        node_list.append(temp_str)
    return node_list

# 无有限级别
def calc_no_priority(node_list):
    '''
    算数都是 left op right
    首先拿出第一个数字赋值给_num_left
    然后每次索引为1的位置每次从node_list拿到两个元素，第一个都为操作符，第二个为right值
    判断操作符，将左值与右值计算，并将结果在赋值给左值
    '''
    _num_left = float(node_list[0])

    for i in range(1, len(node_list), 2):
        _op = node_list[i]
        _num_right = float(node_list[i + 1])
        if _op == '+':
            _num_left += _num_right
        elif _op == '-':
            _num_left -= _num_right
        elif _op == '*':
            _num_left *= _num_right
        elif _op == '/':
            _num_left /= _num_right
    return _num_left


# 有限级别
def calc_priority(node_list):
    num_list = []
    op_list = []
    ops = list('+-*/')
    i = 0
    while i < len(node_list):
        if node_list[i] in ops:
            if len(op_list) == 0:
                op_list.append(node_list[i])
            else:
                #判断op_list[-1] node_list[i]优先级
                #如果当前的优先级比上一次的低就想上次的结果进行运算，否则将操作符append到op_list中
                if op_list[-1] == '+':
                    if node_list[i] == '+' or node_list[i] == '-':
                        #计算
                        num_right = num_list.pop()
                        num_left = num_list.pop()
                        op_list.pop()
                        num_list.append(float(num_left) + float(num_right))
                        i -= 1
                    else:
                        op_list.append(node_list[i])
                elif op_list[-1] == '-':
                    if node_list[i] == '+' or node_list[i] == '-':
                        #计算
                        num_right = num_list.pop()
                        num_left = num_list.pop()
                        op_list.pop()
                        num_list.append(float(num_left) - float(num_right))
                        i -= 1
                    else:
                        op_list.append(node_list[i])
                elif op_list[-1] == '*':
                    #计算
                    num_right = num_list.pop()
                    num_left = num_list.pop()
                    op_list.pop()
                    num_list.append(float(num_left) * float(num_right))
                    i -= 1
                else:
                    #计算
                    num_right = num_list.pop()
                    num_left = num_list.pop()
                    op_list.pop()
                    num_list.append(float(num_left) / float(num_right))
                    i -= 1
        else:
            num_list.append(node_list[i])
        i += 1

    #修正未计算的
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


txt = '1+2*3-5'
node_list = split_str(txt)
print calc_no_priority(node_list)
print calc_priority(node_list)