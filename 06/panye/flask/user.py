USER_LIST = 'users.txt'
CONTENT_DICT = {0: 'name', 1:'passwd', 2:'tel', 3:'gender'}

def get_user():
	_user_dict = {}
	try:
		handle = open(USER_LIST, 'rb')
		for i in handle:
			_nodes = i.split()
			_user = {}
			for t in range(len(_nodes)):
				_user[CONTENT_DICT.get(t)] = _nodes[t]
			_user_dict[_user.get('name')] = _user
		handle.close()
	except BaseException as e:
		print str(e)
	return _user_dict

def get_user_info(name):
	_users = get_user()
	return _users.get(name)


def add_user(name, passwd, tel):
	_user = get_user_info(name)
	if _user is None:
		h = open(USER_LIST, 'ab')
		h.write('%s %s %s\n' % (name, passwd, tel))
		h.close
		return True
	return False

def val_user_login(name, passwd):
	_user = get_user_info(name)
	return (not not _user) and _user.get('passwd') == passwd

def val_user_add(name, passwd, tel):
	if name == '' or passwd == '':
		return False, 'Username and Password are empty'
	
	_user = get_user_info(name)
	if _user is not None:
		return False, 'Username is taken, please change to other name'
	
	return True, ''


if __name__ == '__main__':
	print val_user_login('pye', '123456')
	print val_user_login('py2', '123456')
