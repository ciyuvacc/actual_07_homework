#!/usr/bin/env python
#encoding: utf-8
arr = [2,1,452,234,14]
for i in range(1,len(arr)):
	key =arr[i]
	j = i - 1
	while j >= 0:
		if arr[j] > key:
			arr[j+1] = arr[j]
			arr[j] = key
		else:
			break
		j -= 1
print arr
