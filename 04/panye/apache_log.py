import sys

def split_log(logfile):
    stat_dict = {}
    for line in logfile:
        split_line = line.split()
        remote_host = split_line[0] 
        url = split_line[6]
        status = split_line[8]
        key = (remote_host, url, status)
    
        if key not in stat_dict:
            stat_dict[key] = 1
        else:
            stat_dict[key] = stat_dict[key] + 1

    return stat_dict


def main():
    if not len(sys.argv) > 1:
        print "input your log file"
        sys.exit(1)

    in_file_path = sys.argv[1]
    try:
        infile = open(in_file_path, 'r')
    except IOError:
        print "File does not exsit"
        sys.exit(1)
    
    _relist_dict = {}
    for key, value in split_log(infile).items():
        _key = value
        remote_host, url, status = key
        _value = [status, url, (remote_host, value)]

        if _key not in _relist_dict:
            _relist_dict[_key] = []
        _relist_dict[_key].append(_value)
    
    count_list = _relist_dict.keys()
    for i in range(len(count_list) - 1, -1, -1):
        for t in range(i):
            if count_list[t] < count_list[t+1]:
                count_list[t], count_list[t+1] = count_list[t+1], count_list[t]


    wfile = open("report.txt", "w")
    for count in count_list: 
        for item in _relist_dict[count]:
            wfile.write(str(item) + '\n')
    print "Please check report.txt"


    infile.close()

if __name__ == "__main__":
    main()
