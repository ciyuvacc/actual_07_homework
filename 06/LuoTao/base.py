

def count_log(infile,node):
  'count for log (infile,node)'
  handle = open(infile)
  log_stat_dict = {}
  while True:
      _line = handle.readline()
      if '' == _line:
          break
      _log_nodes = _line.split()
      _ip = _log_nodes[0]
      _url = _log_nodes[6]
      _code = _log_nodes[8]
      _key = (_ip, _url, _code)
      log_stat_dict.setdefault(_key, 0)
      log_stat_dict[_key] += 1
  handle.close()  

  log_stat_list = []  
  for _key in log_stat_dict:
      _value = log_stat_dict[_key]
      _ip, _url, _code = _key
      log_stat_list.append([_code, _url, (_ip, _value)])

  if node <=1:
     node=2
  elif node >len(log_stat_list):
    node = len(log_stat_list) -1
  for j in range(len(log_stat_list)-1):
      if j >= node: 
          break
      for i in range(len(log_stat_list) - 1 - j): 
          if log_stat_list[i][2][1] > log_stat_list[i+1][2][1]:
              log_stat_list[i], log_stat_list[i+1] = log_stat_list[i+1], log_stat_list[i]
  return log_stat_list[:-(node):-1],len(log_stat_list)

def sys_pass():
    path='./passfile'
    hd1=open(path, 'r')
    tmp_dict={}
    for _line in hd1:
        arr=_line.split()
        tmp_dict[arr[0]]={'password':arr[1],'email':arr[2],'sex':arr[3],'age':arr[4]}
    hd1.close()
    return tmp_dict
def sys_writepass(pass_dict):
    path='./passfile'
    hd2=open(path, 'w')
    for _key, _value in pass_dict.items():
       hd2.writelines([_key,' ', _value['password'],' ',_value['email'],' ',_value['sex'],' ',_value['age'], '\n'])
    hd2.close()


def sys_dml(user ,pwd, change):
    pass_dict=sys_pass()
    message = ''
    if user == '' or pwd == '': 
        message = 'User or passwd is null'
    else:
        if change == 'ADD':
            if user not in pass_dict:
                pass_dict[user] = pwd 
                message = 'User add success'
                sys_writepass(pass_dict)
            else:
                message = 'User %s already exist' % user
        elif change == 'delete':
            pass_dict.pop(user)
            message = 'User delete success'
            sys_writepass(pass_dict)
        elif change == 'update':
            pass_dict[user] = pwd
            message = 'User update success'
            sys_writepass(pass_dict)

    return pass_dict ,message

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
    for a in range(0,len(tmp_list)-1,2):
      if a == 0:
        tmp_count=eval(tmp_list[a]+tmp_list[a+1]+tmp_list[a+2])
      else:
        tmp_count =eval(str(tmp_count)+tmp_list[a+1]+tmp_list[a+2])
      num_count = tmp_count  

    return num_count
