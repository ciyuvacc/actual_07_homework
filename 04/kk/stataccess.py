#encoding: utf-8

'''
思路
1. 了解文件内容格式
2. 从文件中解析一行数据，得到IP, url, Code
3. 遍历文件, 解析每一行数据
4. 统计, 按照key=>value的形式存储统计结果, key使用IP, url, Code的组合, 因此选择使用tuple(IP, url, code), value用做计数
5. 转换统计的dict格式成咱们要的List形式, 使用相同元素数量的变量接收字典的key, 得到IP, url, code, count=>value, 组合新的数据格式
6. 排序(冒泡) ==> 时间(有耐心的同学可以等等，计算下时间), 也可以选择其他排序算法
7. 排序的元素太多? 速度太慢? 想其他方法? 
    统计字符串出现次数top 10时，咱们按照出现次数统计了对应出现的字符都有哪些?
    {
        20 : ['a', 'y', 'z'],
        50 : ['e', 'f'],
        1 : ['!'],
    }
    咱们对出现次数排序, 然后从dict中找到TOP10出现次数最多的字符
8. 统计次数对应的dict, value为咱们要的结果[code, url, (ip, code)]
9. 对获取所有统计次数进行排序, 从大到小依次获取dict中的数据，使用print打印
10. 将数据按出现次数从大到小的顺序写入文件
'''

'''
#1. 了解文件内容格式
#2. 从文件中解析一行数据，得到IP, url, Code

logtext = '111.85.25.71 - - [23/Aug/2014:00:07:12 +0800] "GET /public/themes/adreambox/images/user_pic_middle.gif HTTP/1.1" 304 \ "http://www.adreambox.net/index.php?app=home&mod=Space&act=index&uid=8403" "Mozilla/5.0 (iPad; CPU OS 6_1_3 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10B329 Safari/8536.25" "-"'

log_list = logtext.split(' ')

ip = log_list[0]
url = log_list[6]
code = log_list[8]

print ip, url, code
'''

stat_dict = {}

handle = open('www_access_20140823.log', 'r')

# 3. 遍历文件, 解析每一行数据
# 4. 统计, 按照key=>value的形式存储统计结果, key使用IP, url, Code的组合, 因此选择使用tuple(IP, url, code), value用做计数
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

'''

# 5. 转换统计的dict格式成咱们要的List形式, 使用相同元素数量的变量接收字典的key, 得到IP, url, code, count=>value, 组合新的数据格式
# 6. 排序(冒泡) ==> 时间(有耐心的同学可以等等，计算下时间)
stat_list = []

for key, value in stat_dict.items():
    ip, url, code = key
    stat_list.append([code, url, (ip, value)])

# 6. 排序(冒泡) ==> 时间(有耐心的同学可以等等，计算下时间), 也可以选择其他排序算法
# 7. 排序的元素太多? 速度太慢? 想其他方法? 
print len(stat_list) #44093 44092 * 44092 
for j in range(len(stat_list) - 1):
    for i in range(len(stat_list) - 1):
        if stat_list[i][2][1] < stat_list[i + 1][2][1]:
            stat_list[i], stat_list[i + 1] = stat_list[i + 1], stat_list[i]

print stat_list[:10]
'''


'''
{
20 : ['a', 'b', 'c'],
10 : ['d']
}
'''

# 8. 统计次数对应的dict, value为咱们要的结果[code, url, (ip, code)]
stat_count_dict = {}

for key, value in stat_dict.items():
    new_key = value 
    ip, url, code = key
    new_value = [code, url, (ip, value)]
    if new_key not in stat_count_dict:
        stat_count_dict[new_key] = []
    stat_count_dict[new_key].append(new_value)

#9. 对获取所有统计次数进行排序, 从大到小依次获取dict中的数据，使用print打印
count_list = stat_count_dict.keys()

for j in range(len(count_list) - 1):
    for i in range(len(count_list) - 1):
        if count_list[i] < count_list[i + 1]:
            count_list[i], count_list[i + 1] = count_list[i + 1], count_list[i]


# print count_list

# 10. 将数据按出现次数从大到小的顺序写入文件
handle = open('rs.txt', 'w')
for count in count_list:
     for item in stat_count_dict[count]:
         handle.write(str(item) + '\n')

handle.close()

print 'over'

