def Sum_str(n1,n2,op):
    Sum = 0
    n1,n2 = int(n1),int(n2)
    if op == '+':
        Sum = n1 + n2
    elif op == '-':
        Sum = n1 - n2
    elif op == '*':
        Sum = n1 * n2
    elif op == '/' and n2 != 0:
        n1,n2 = float(n1),float(n2)
        Sum = n1 / n2
    return Sum

def Sum_list(str):
    op_str = ('+','-','*','/')
    _index = 0
    i = 0
    global tmp_list
    tmp_list = []
    for x in str:
        if x in op_str:
            tmp_list.append(str[_index:i])
            _index = i
        i += 1
    tmp_list.append(str[_index:])
    return tmp_list

str1 = raw_input("Please enter an expression:")
#str1 = '1+2+4-3*7/3'
print str1
Sum_list(str1)
Sum = tmp_list[0]
for n in range(1,len(tmp_list)):
    Sum = Sum_str(Sum,tmp_list[n][1:],tmp_list[n][0])
print '%s = %.2f' % (str1,Sum)
