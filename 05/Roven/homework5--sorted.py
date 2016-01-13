def max1(x):
  tmp=x[0]
  if x[0] < x[1]:
    tmp =x[1]
  return tmp

arr=[(1, 4), (5, 1), (2, 3), (4, 2),(2, 1)]
print sorted(arr, key=lambda x:(max(x)))
print sorted(arr, key=lambda x:(max1(x)))
print sorted(arr, key=lambda x:( x[0] / x[1] and x[0] or x[1]))
print sorted(arr, key=lambda (x,y):(x*(x>y)+y*(x<=y)))
print sorted(arr, cmp=lambda x,y:max(x) > max(y) and 1 or -1)
print sorted(arr, cmp=lambda x,y: x[0]*(x[0]>x[1])+x[1]*(x[0]<=x[1]) > y[0]*(y[0]>y[1])+y[1]*(y[0]<=y[1]) and 1 or -1)
print sorted(arr, cmp=lambda x,y: (x[0] / x[1] and x[0] or x[1]) > (y[0] / y[1] and y[0] or y[1]) and 1 or -1)
