__author__ = 'XuHeng'
#
#试写 第一版本
#

read_me = '''
first of all, i want make it clear that i can not claim understanding this holy book  in just a few weeks, and i would not dare comment on this sacred book, in addition, i don't think i can give you a full picture of the holy bible in just few words.i can not preach anything here. what i want to do here is to express my understanding by sharing two events described in this book. the fist story i want to share is abandoned tower of babel.according to the bibel,people use the same language to communicate with each other in ancient times.with the soaring vanity,they decided to build a heaven-reaching tower to show off their achievement, god knows, he change the human language into different kinds and make it difficult for people to communicate with each other,hence the failure of building tower of  babel.this story tells people,never do things in selfishness, but make a life out of enternal glory.the other story,before jesus christ was crucified,he said, father,forgive them, for they know not what they do. with great love, he shouldered all the sins of  people. what can we learn from this story?we live in this world thanks to the love of god, for this reanson, we should make our lives glorious to honor our god.finally,i want to sum up by saying that only if we put our lives in the eternal love of god,can we live a perfect life, and  what you appealed is what god expected!
'''
str_list={}
num_list=[]
res_list={}
for a in read_me:
        str_list[a]=str_list.setdefault(a,0)+1
print str_list

for k,v in str_list.items():
    num_list.append(v)
print num_list

for i in sorted(num_list)[-10:]:
    for k,v in str_list.items():
        if i == v:
            res_list[k]=v
print res_list

#print sorted(str_list.items(),key=lambda e:e[1],reverse=True)[:10]




'''
想法是对的，但是考虑一下，如果read_me中有26个字符，且都出现一次，是将这26个字符都打印出来呢？可以怎么改进下

'''



