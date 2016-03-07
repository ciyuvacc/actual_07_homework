#encoding: utf-8
class Ainmal(object):
    def __init__(self, name, age='1'):
    	print 'Ainaml init'
        self.__name = name
        self.__age = age

    def run(self):
        print self.__name + ' run'

    def eat(self):
        print self.__name + ' eat'


class Dog(Ainmal):
    def __init__(self, name, age, variety):
        print 'Dog init'
        super(Dog, self).__init__(name, age)
        self.__variety = variety


class Person(Ainmal):
    def __init__(self, name, age, skin):
        super(Person, self).__init__(name, age)
        self.__skin = skin
        self.__name = name

    def say(self):
        print 'say'

    def eat(self):
        print self.__name + ' 站着吃'


class A(object):
     def __init__(self, name):
         print 'A init'
         self._name = name

     def print_name(self):
         print self._name

class B(A):
      def print_name(self):
          print 'B' + self._name 
