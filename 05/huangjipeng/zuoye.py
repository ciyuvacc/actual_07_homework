#!/usr/bin/env python
#encoding:utf-8
#zuoye1
_list = [(1,4),(5,1),(2,3),(1,2)]

def _get_max(x):
    return x[0] if x[0] > x[1] else x[1]
def _cmp_element(x1,x2):
    max_x1 = _get_max(x1)
    max_x2 = _get_max(x2)
    return max_x1 > max_x2


if __name__ == '__main__':    
    for j in range(len(_list) -1):
        for i in range(len(_list) -1):
            if _cmp_element(_list[i],_list[i +1]):
                _list[i],_list[i + 1] = _list[i + 1],_list[i]
    print _list 
    print sorted(_list,key=_get_max)
    print sorted(_list,key=lambda x:(sorted(x))[1])

    print sorted(_list,key=lambda x:max(x))

    print sorted(_list,key=max)


#zuoye2

def log_count_dict(log_path):
    log_dict = {}
    log_file = open(log_path,'r')
    for file_line in log_file:
        line_list = file_line.split(' ')
        try:
            _ip = line_list[0]
            _url = line_list[6]
            _code = line_list[8]
            _key = (_ip,_url,_code)
            log_dict.setdefault(_key,0)
            log_dict[_key] += 1
        except BaseException as e:
            with open('error.log','a') as fd:
                print >> fd,e
            continue
    log_file.close()
    return log_dict
def log_list(log_dict,n):
    log_list = []
    for _key in log_dict:
        _ip,_url,_code = _key
        _value = log_dict[_key]
        log_list.append([_code,_url,(_ip,_value)])
    new_log_list = sorted(log_list,reverse=True,key=lambda x:x[2][1])
    #for j in new_log_list[:n-1]:    
 #   print j 
    return new_log_list[:n-1]
def log_write(Path,sort_list):
    txt = open(Path,'w')
    for i in sort_list:
        #x = '|'.join(i)
        txt.write(str(i) +'\n')
    txt.close()

def log_print(sort_list):
    for x in sort_list:
       print x     
def run(file_log='access.log',n=10):
    a = log_count_dict(file_log)
    sort_list = log_list(a,n)
    log_write('sort_log.txt',sort_list)
    log_print(sort_list)
##zuoye3
def split_expr(expr):
    num_str = ''
    expr_list = []
    for ch in expr:
        if ch in '+-*/':
            try:
                expr_list.append(num_str)
                expr_list.append(ch)
            except:
                continue
            num_str = ''           
        else:
            num_str += ch
    if '' != num_str:
        expr_list.append(num_str)
    return expr_list

def add_(left,right):
    return float(left) + float(right)

def sub_(left,right):
    return float(left) - float(right)

def mul_(left,right):
    return float(left) * float(right)

def div_(left,right):
    return float(left) / float(right)

op_dict =  {'+' : add_,
            '-' : sub_,
            '*' : mul_, 
            '/' : div_
           # '/' : lambda lift,right:left / right
   }

def expr_op(expr_list):
    left_num = expr_list[0]
    step = 2
    for i in range(1,len(expr_list), step):
        op = expr_list[i]
        try:
            right_num = expr_list[i + 1]
            left_num = op_dict[op](left_num,right_num)
        except:
            continue
    return left_num

def op_run():
    expr_str = "*/12+2*3-5/2-333/"
    expr_list = split_expr(expr_str)
    return expr_op(expr_list)

#print op_run()

def expr_op2(expr_list):
    num_list =[]
    op_list = []
   # print expr_list
    for i in range(len(expr_list)):
        node  = expr_list[i]
        if node not in '+-*/':
            num_list.append(node)
        else:
            if len(op_list) == 0:
                op_list.append(node)
            else:
                if node == '+' or node == '-' or node == '*' and (op_list[-1] == '*' or op_list[-1] == '/') or \
                   node == '/' and (op_list[-1] == '*' or op_list[-1] == '/'):
                    op = op_list.pop()
		    right_num = num_list.pop()
                    left_num = num_list.pop()
                    result = op_dict[op](left_num,right_num)
                    num_list.append(result)
                    op_list.append(node)
                else:
                    op_list.append(node)
    #print op_list
    #print num_list
    # 计算剩下的没计算过的	
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
if __name__ == "__main__":
    print "1234567890"
    run()

    expr = '1+3+4+5*10+2+5*4'
    expr_list = split_expr(expr)
    print expr_op2(expr_list)
