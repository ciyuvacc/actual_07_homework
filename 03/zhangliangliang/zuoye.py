#encoding=utf-8
# 统计字符数量之后，打印出现次数前10的字符
read_me = '''
first of all, i want make it clear that i can not claim understanding this holy book  in just a few weeks, and i would not dare comment on this sacred book, in addition, i don't think i can give you a full picture of the holy bible in just few words.i can not preach anything here. what i want to do here is to express my understanding by sharing two events described in this book. the fist story i want to share is abandoned tower of babel.according to the bibel,people use the same language to communicate with each other in ancient times.with the soaring vanity,they decided to build a heaven-reaching tower to show off their achievement, god knows, he change the human language into different kinds and make it difficult for people to communicate with each other,hence the failure of building tower of  babel.this story tells people,never do things in selfishness, but make a life out of enternal glory.the other story,before jesus christ was crucified,he said, father,forgive them, for they know not what they do. with great love, he shouldered all the sins of  people. what can we learn from this story?we live in this world thanks to the love of god, for this reanson, we should make our lives glorious to honor our god.finally,i want to sum up by saying that only if we put our lives in the eternal love of god,can we live a perfect life, and  what you appealed is what god expected!
'''
# 1、定义一个空字典,遍历read_me,遍历的字符为key ，出现的次数为value
# 2、判断key在count_dict是否存在，如果不存在，value为0，执行value += 1;如果存在跳过设置默认值,执行value += 1
# 3、将count_dict转为列表形式，比较value大小进行插入排序，翻转排好序的列表并打印前10
count_dict = {}
for key in read_me:
    count_dict.setdefault(key,0)
    count_dict[key] += 1

count_list = count_dict.items()
for i in range(1,len(count_list)):
    for idx in range(i,0,-1):
        if count_list[idx][1] < count_list[idx-1][1]:
            count_list[idx],count_list[idx-1] = count_list[idx-1],count_list[idx]
print "================ 统计排序 ==============="
print count_list
print "================ 排名前十 ==============="
print count_list[::-1][0:10]



'''
不错，思路很清晰，结果正确
使用dict对字符串中的字符计数
使用setdefault初始化字符个数
使用插入排序对每个元素的都是tuple的list进行从小到大排序
使用切片获取排序后列表的前十位

继续加油，可以在完成的基础功能之上给自己添加点障碍
比如如果前20个字符的数量都相同呢？我们可以指定一个规则比如按字母a到z的顺序找到前10个
比如如果read_me中有大小写的字符呢？我们不区分大小写时如何统计


'''
