#encoding: utf-8


# 比较list中的两个元素,第一个大则范围True
def _cmp_tuple(tuple1, tuple2):
    return _get_tuple_max(tuple1) > _get_tuple_max(tuple2)

#获取每个元素中最大的值
def _get_tuple_max(tuple_ele):
    if tuple_ele[0] > tuple_ele[1]:
        return tuple_ele[0]
    else:
        return tuple_ele[1]

# 仍然使用冒泡
def _sort_list():
    tuple_list = [(1, 4), (5, 1), (2, 3)]

    for j in range(len(tuple_list) - 1):
        for i in range(len(tuple_list) - 1): #将第N(从0起)个最大的数字冒泡到最后
            if _cmp_tuple(tuple_list[i], tuple_list[i + 1]): #比较相邻的两个元素，如果前面比后面大则返回True, 否则为False
                 tuple_list[i], tuple_list[i + 1] = tuple_list[i + 1], tuple_list[i]

    print tuple_list

# 使用sorted+key
def _sort_list2():
    tuple_list = [(1, 4), (5, 1), (2, 3)]
    print sorted(tuple_list, key=_get_tuple_max)
    #将key定义的函数_get_tuple_max写成lambda函数
    print sorted(tuple_list, key=lambda x: x[0] if x[0] > x[1] else x[1])
    #将key定义的函数lambda函数中的判断修改为max
    print sorted(tuple_list, key=lambda x: max(x))


# 比较list中的两个元素,第一个大则返回1，第二个大则返回-1，否则返回0
def _cmp_tuple2(tuple1, tuple2):
    _max_num_1 = _get_tuple_max(tuple1) 
    _max_num_2 = _get_tuple_max(tuple2)
    if _max_num_1 > _max_num_2:
        return 1
    elif _max_num_1 < _max_num_2:
        return -1
    else:
        return 0


# 使用sorted+cmp
def _sort_list3():
    tuple_list = [(1, 4), (5, 1), (2, 3)]
    print sorted(tuple_list, cmp=_cmp_tuple2)
    #将cmp定义的函数_cmp_tuple2写成lambda函数
    print sorted(tuple_list, cmp=lambda x, y: 1 if _get_tuple_max(x) > _get_tuple_max(y) else (-1 if _get_tuple_max(x) < _get_tuple_max(y) else 0))

    #将cmp中定义的函数_get_tuple_max写成max函数
    print sorted(tuple_list, cmp=lambda x, y: 1 if max(x) > max(y) else (-1 if max(x) < max(y) else 0))

_sort_list()
_sort_list2()
_sort_list3()