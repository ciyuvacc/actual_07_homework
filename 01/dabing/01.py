#coding:utf-8

"""鎵撳嵃鐢ㄦ埛杈撳叆"""
"""name = raw_input("Please input your username: ")
if name == 'dabing':
	print "welcome %s" % name
elif  name == 'dahai':
	print  "welcome %s" % name
else:
	print "you are good boy,%s" % name"""

"""
times = 0
sum = 0
num = 0
while num != '':
	num = raw_input("Please input your num: ")
	if num != '':
		sum += int(num)
		times += 1
print sum * 1.0 / times"""

"""total = 10000
n = 0
while  total < 20000:
	total = total * (1 + 0.0325)
	print  n,total
	n += 1

print n"""


l = [1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45]
print sorted(l)[-2],sorted(l)[-1]
"""
if len(l) < 2:
	print "鍒楄〃闀垮害涓嶅..."
else:
	if l[0] > l[1]:   ###鍒ゆ柇绗竴涓拰绗簩涓厓绱犵殑澶у皬骞跺鍒剁粰min鍜宮ax
		min = l[1]
		max = l[0]
		for i in range(1,len(l)-1):  ##閬嶅巻list
			if l[i] > min and l[i] < max:   ##鍏冪礌姣攎in澶ф瘮max灏忥紝鎶婅鍏冪礌澶嶅埗缁檓in锛宮ax涓嶅彉
				min = l[i]
				max = max
			elif l[i] > min and l[i] > max: ##鍏冪礌姣攎ax澶э紝min鍜宮ax浜掓崲锛屾妸鍏冪礌璧嬬粰max
				max,min = min,max
				max = l[i]
			else:                        ##姣攎in灏忥紝浠€涔堥兘涓嶅仛
				pass
	else:
		min = l[0]
		max = l[1]
		for i in range(1,len(l)-1):   ##鍚屼笂
			if l[i] > min and l[i] < max:
				min = l[i]
				max = max
			elif l[i] > min and l[i] > max:
				max,min = min,max
				max = l[i]
			else:
				pass
print min,max  """
