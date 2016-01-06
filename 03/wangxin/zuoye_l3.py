read_me = '''
first of all, i want make it clear that i can not claim understanding this holy book  in just a few weeks, and i would not dare comment on this sacred book, in addition, i don't think i can give you a full picture of the holy bible in just few words.i can not preach anything here. what i want to do here is to express my understanding by sharing two events described in this book. the fist story i want to share is abandoned tower of babel.according to the bibel,people use the same language to communicate with each other in ancient times.with the soaring vanity,they decided to build a heaven-reaching tower to show off their achievement, god knows, he change the human language into different kinds and make it difficult for people to communicate with each other,hence the failure of building tower of  babel.this story tells people,never do things in selfishness, but make a life out of enternal glory.the other story,before jesus christ was crucified,he said, father,forgive them, for they know not what they do. with great love, he shouldered all the sins of  people. what can we learn from this story?we live in this world thanks to the love of god, for this reanson, we should make our lives glorious to honor our god.finally,i want to sum up by saying that only if we put our lives in the eternal love of god,can we live a perfect life, and  what you appealed is what god expected!
'''
'''
dict1 = {}
for i in read_me:
  if i == '' or i == '\n' or i == ' ':
    continue
  if i not in dict1:
    dict1[i] = 1
  else:
    dict1[i] = dict1[i] +1
print dict1
'''

dict1 = {}
for i in read_me:
    dict1.setdefault(i,0)
    dict1[i] += 1

list1 = dict1.items()
for i in range(1,len(list1)):
    for j in range(i,0,-1):
	if (list1[j])[1] < (list1[j -1])[1]:
            list1[j],list1[j - 1 ] = list1[j - 1 ],list1[j]
        else:
            break
print list1[-1:-11:-1]



'''
不错，结果是正确的

1. 注意文件中的缩进方式使用4个空格，尽量不要使用tab键，可能导致在不同的编辑器中看到的缩进不一致，导致脚本不能运行
2. (list1[j])[1] ==> list1[j][1]

'''

    