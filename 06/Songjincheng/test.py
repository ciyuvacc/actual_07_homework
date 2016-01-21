'''
def file_name(name):
    data_name = {}
    with open(name,'r') as handle:
        while True:
            filename = handle.readline()
            if '' == filename:
                break
            name = filename.split()
            username = name[0]
            password = name[1]
            data_name[username] = password
    print data_name
'''

def filename(name):
    data_list = []
    with open(name,'r') as handle:
        while True:
            filename = handle.readline()
            if '' == filename:
                break
            name_list = filename.split()
            data_list.append(name_list)
    for i in data_list:
        print i[0]





filename('name.txt')
