#!/usr/bin/python
#-*- coding: utf-8 -*-

def sortList(argvlist):
    """This function is used to sort list by insertion algorithm"""
    try:
        if type(argvlist) != list or len(argvlist) < 1:
            print('The parameter must be list and the list length is larger than 1!') 
        else:
            #Insertion algorithm
            for i in range(1,len(argvlist)):
                contrast = argvlist[i]
                while i > 0 and int(contrast) < int(argvlist[i-1]):
                    argvlist[i] = argvlist[i-1]
                    i -= 1
                argvlist[i] = contrast
            return argvlist
            
    except:
        print('The list exist a element not a number!')
        return -1


if __name__ == '__main__':

    templist = '''first of all, i want make it clear that i can not claim understanding this holy book  in just a few weeks, and i would not dare comment on this sacred book, in addition, i don't think i can give you a full picture of the holy bible in just few words.i can not preach anything here. what i want to do here is to express my understanding by sharing two events described in this book. the fist story i want to share is abandoned tower of babel.according to the bibel,people use the same language to communicate with each other in ancient times.with the soaring vanity,they decided to build a heaven-reaching tower to show off their achievement, god knows, he change the human language into different kinds and make it difficult for people to communicate with each other,hence the failure of building tower of  babel.this story tells people,never do things in selfishness, but make a life out of enternal glory.the other story,before jesus christ was crucified,he said, father,forgive them, for they know not what they do. with great love, he shouldered all the sins of  people. what can we learn from this story?we live in this world thanks to the love of god, for this reanson, we should make our lives glorious to honor our god.finally,i want to sum up by saying that only if we put our lives in the eternal love of god,can we live a perfect life, and  what you appealed is what god expected!'''
    tempdict = {}
    for key in templist:
        tempdict.setdefault(key,0)
        tempdict[key] += 1

    #No.1
    newlist = []
    for key, value in tempdict.items():
        newlist.append((key, value))

    for i in range(1,len(newlist)):
        contrast = newlist[i]
        while i > 0 and contrast[1] < newlist[i-1][1]:
            newlist[i] = newlist[i-1]
            i -= 1
        while i > 0 and contrast[1] == newlist[i-1][1] and ord(contrast[0]) > ord(newlist[i-1][0]):
            newlist[i] = newlist[i-1]
            i -= 1
        newlist[i] = contrast

    print [i[0] for i in newlist[:-11:-1]]
                
    #No.2
    revtempdict = {}
    charcount = 0
    charlist = []
    for key, value in tempdict.items():
        revtempdict.setdefault(value,[])
        revtempdict[value].append(ord(key))

    for key in sortList(revtempdict.keys())[::-1]:
        if charcount < 10:
           charlist.extend(sortList(revtempdict[key]))
           charcount += len(revtempdict[key])

    print [chr(i) for i in charlist][:10]
     



'''
不错，尝试了两种方法结果也正确
而且使用了字符和ascii转换的函数ord和chr，列表生成器，函数等相关知识，自己可以学习新的知识点，很棒

方法一：
有几个可以改进的地方
1. 可以打印看看tempdict.items()和执行第34和35行后的newlist有什么不同
2. 第42行字符串也是可以进行大小计较，结果和使用ord计算其对应ascii比较结果相同


'''