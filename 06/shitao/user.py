#!/usr/bin/env python
def get_user(userfile):
    _list = []
    with open(userfile,'r') as f:
        for line in f:
            newline = line.split()
            name = newline[0]
	    passwd = newline[1]
            email = newline[-1]
	    vv = (name,passwd,email)
	    _list.append(vv)
	return _list
if __name__ == "__main__":
    get_user('user.txt')
