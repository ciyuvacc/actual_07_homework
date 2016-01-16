def get_max_num(mylist):
	if mylist[0] > mylist[1]:
		return mylist[0]
	else:
		return mylist[1]


def sort_list():
	mylist = [(1, 4), (5, 1), (2, 3)]
	print sorted(mylist, key=get_max_num)


def sort_lambda():
	mylist = [(1, 4), (5, 1), (2, 3)]
	print sorted(mylist, key=lambda x: x[0] if x[0] > x[1] else x[1])

def sort_max():
	mylist =  [(1, 4), (5, 1), (2, 3)] 
	print sorted(mylist, key=lambda x: max(x))	

sort_list()
sort_lambda()
sort_max()
