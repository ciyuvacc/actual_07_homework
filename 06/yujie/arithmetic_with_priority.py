#!/bin/env python
# -*- encoding:utf-8 -*-
# arithmetic_with_priority.py
# Author : Jacob.Yu
# CTime : 2016-01-17

# Task 3
# level 2
# 从字符串中拆分出数字和运算符
def split_expr(expr):
    expr_list = []
    num_str = ''
    for ch in expr:
        if ch not in '+-*/':
            num_str += ch
        else:
            expr_list.append(num_str)
            num_str = ''
            expr_list.append(ch)
    if num_str != '':
        expr_list.append(num_str)
    return expr_list

# 利用字典存储字符串和对应操作函数的关系
add_func = lambda left,right: left + right
sub_func = lambda left,right: left - right
mul_func = lambda left,right: left * right
div_func = lambda left,right: left / right

op_func_dict = {
    '+':add_func,
    '-':sub_func,
    '*':mul_func,
    '/':div_func
}

# 带优先级的运算
def arithmetic_with_priority(expr_list):
    num_list = []
    op_list = []

    for i in range(len(expr_list)):
        node = expr_list[i]
        if node not in '+-*/':
            num_list.append(node)
        elif len(op_list) == 0:
            op_list.append(node)
        elif node == '+' or \
            node == '-' or \
            node == '*' and (op_list[-1] == '*' or op_list[-1] == '/') or \
            node == '/' and (op_list[-1] == '*' or op_list[-1] == '/'):
            op = op_list.pop()
            right_num = num_list.pop()
            left_num = num_list.pop()
            result = op_func_dict[op](float(left_num),float(right_num))
            num_list.append(result)
            op_list.append(node)
        else:
            op_list.append(node)
    #print num_list
    #print op_list

    # 此处存在bug，如expr_str = '2+2-10/2-5'时，会出现结果是4，但是正确结果却是-6
    # 因为最后在num_list和op_list中组成的计算式是：4-5-5，若直接从后取数字计算，则会违背同级运算符从左到右计算的原则，导致计算结果出错
    while len(op_list) > 0:
        op = op_list.pop()
        right_num = num_list.pop()
        left_num = num_list.pop()
        result = op_func_dict[op](float(left_num),float(right_num))
        num_list.append(result)
    return num_list[0]

if __name__ == '__main__':
    #expr_str = '12+2*3-5-13'
    #expr_str = '2-6/3+5*2'
    expr_str = '2+2-10/2-5'
    #expr_str = '2-2+4-10/2-5'
    expr_list = split_expr(expr_str)
    print arithmetic_with_priority(expr_list)