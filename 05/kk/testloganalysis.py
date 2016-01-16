#encoding: utf-8

# path = 'www_access_20140823.log'
# 将读取log文件封装成函数
# @param str path log文件路径
# @param dict 日志中按照ip url code统计的次数
def read_log(path):
    stat_dict = {}

    handle = open(path, 'r')
    for line in handle:
        line_list = line.split(' ')
        ip = line_list[0]
        url = line_list[6]
        code = line_list[8]

        key = (ip, url, code)
        if key not in stat_dict:
            stat_dict[key] = 1
        else:
            stat_dict[key] = stat_dict[key] + 1

    handle.close()
    return stat_dict

#将获取top10 封装成函数
# @param dict stat_dict ip, url, code 统计的次数
# @param int n 需要获取的top n, 若为-1则获取全部
def stat_top_n(stat_dict, n=-1): 
    stat_count_dict = {}

    for key, value in stat_dict.items():
        new_key = value 
        ip, url, code = key
        new_value = [code, url, (ip, value)]
        if new_key not in stat_count_dict:
            stat_count_dict[new_key] = []
        stat_count_dict[new_key].append(new_value)

    count_list = stat_count_dict.keys()

    for j in range(len(count_list) - 1):
        for i in range(len(count_list) - 1):
            if count_list[i] < count_list[i + 1]:
                count_list[i], count_list[i + 1] = count_list[i + 1], count_list[i]

    result_list = []
    result_idx = 0
    for count in count_list:
        for item in stat_count_dict[count]:
            result_list.append(item)
            result_idx += 1
            if n > 0 and result_idx >= n:
                break

    return result_list


# 将结果写入文件
# @param str path 写入文件位置
# @param list item_list topn的数据
def write_log(path, item_list):
    # 10. 将数据按出现次数从大到小的顺序写入文件
    handle = open('rs.txt', 'w')
    for item in item_list:
        handle.write(str(item) + '\n')
    handle.close()

# 打印结果到控制台
# @param list item_list topn的数据
def print_log(item_list):
    for item in item_list:
        print item

def run():
    stat_dict = read_log('access.log')
    item_list = stat_top_n(stat_dict, 10)
    write_log('rs.txt', item_list)
    print_log(item_list)

run()
