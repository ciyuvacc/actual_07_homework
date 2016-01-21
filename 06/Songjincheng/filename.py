#!/usr/bin/env python


with open(name,'r')as handle:
    while True:
        filename = handle.readline()
        if '' == filename:
            break
        name = filename.split()
        username = name[0]
        password = name[1]
        data_name[username] = password
        returni data_name



f = file('name.txt','r')
for line in f.readlines():
    line = line.split()
#    for i in line:
    username = line[0]
    password = line[1]
    if 'liu' == username and '123456' == password:
        print "OK"
        break




