#base module
def count_log(infile):
  'count for log (infile)'
  handle = open(infile)
  log_stat_dict = {}
  handle1 = open('./log_tag','r+')
  log_tag = handle1.readline()
  handle1.close()  
  if log_tag !=  '':
      log_tag= int(log_tag)
      handle.seek(log_tag)
  for _line in handle.xreadlines():
      _log_nodes = _line.split()
      _ip = _log_nodes[0]
      _url = _log_nodes[6]
      _code = _log_nodes[8]
      _key = (_ip, _url, _code)
      log_stat_dict.setdefault(_key, 0)
      log_stat_dict[_key] += 1
  log_tag=handle.tell()
  handle.close()  
  handle1 = open("./log_tag",'w+')
  print "log_tag is %s" % log_tag
  handle1.write(str(log_tag))
  handle1.close()  
  return log_stat_dict


def init_func1(mystr):
    arr=list(mystr)
    if arr[0] == '-':
      arr.pop(0)
      arr[0]= '-'+arr[0] 
    tmp_list=[] 
    tmpstr=''
    i=0  
    while i < len(arr):
      if arr[i] in '+-*/':
        tmp_list.append(tmpstr)
        tmp_list.append(arr[i])
        tmpstr=''
        i += 1
      else:
        tmpstr=tmpstr + arr[i]
        i += 1
    tmp_list.append(tmpstr)  
    if len(tmp_list) >=5:
      j=3
      tmp_list1=[]
      result1 =[]
      while j <len(tmp_list)-1:
        if tmp_list[j] in '*/':
          tmp_list1.append(tmp_list.pop(j-1))
          tmp_list1.append(tmp_list.pop(j-1))
          if len(tmp_list)-1 <j:
            tmp_list1.append(tmp_list[j-1])
            count1 =operate3(tmp_list1)
            tmp_list[j-1]=str(count1)
            break
          if tmp_list[j] in '+-':
            tmp_list1.append(tmp_list[j-1])
            count1 =operate3(tmp_list1)
            tmp_list[j-1]=str(count1)
            tmp_list1 =[]
        else:
          j += 2
    return operate3(tmp_list)
def operate3(tmp_list): 
    if len(tmp_list) == 1: 
      return tmp_list[0]
    tmp_count=0
    num_count=0
    op_dict = {
       '+':lambda x,y: x+y,
       '-':lambda x,y: x-y,
       '*':lambda x,y: x*y,
       '/':lambda x,y: x/y
    }
    for a in range(0,len(tmp_list)-1,2):
      if a == 0:
          tmp_count=tmp_list[a]
      tmp_count=op_dict[tmp_list[a+1]](float(tmp_count),float(tmp_list[a+2]))

    return tmp_count 

