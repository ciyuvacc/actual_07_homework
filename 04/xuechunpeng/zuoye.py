stat_dict = {}

handle = open('www_access_20140823.log','r')

for line in handle:
    line_list = line.split(' ')
    ip = line_list[0]
    url = line_list[6]
    code = line_list[8]

    key = (ip, url, code) 
    if key not in stat_dict:
        stat_dict[key] = 1
    else:
        stat_dict[key] +=1

handle.close() 

'''
dict change to list
'''

stat_list = []

for key,value in stat_dict.items():
    ip,url,code = key
    stat_list.append([code, url,(ip,value)])

'''
sort
'''
print len(stat_list)
for j in range(len(stat_list) - 1):
    for i in range(len(stat_list) - 1):
        if stat_list[i][2][1] <stat_list[i + 1][2][1]:
            stat_list[i],stat_list[i+1] = stat_list[i+1],stat_list[i]
print stat_list[:10]


