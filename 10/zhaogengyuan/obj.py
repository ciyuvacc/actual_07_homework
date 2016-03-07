#encoding: utf-8
class Animal(object):
    
    incr = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Animal.incr += 1
        print '__init__', Animal.getIncr()

    def run(self):
        print '%s run' % self.name

    def eat(self):
        print 'eat'

    def cry(self):
        print 'cry'
        self.eat()
   
    @classmethod
    def getIncr(cls):
        return cls.incr
    
    @staticmethod 
    def print_args(*args, **kwargs):
        print args, kwargs

class Plant(object):
    pass

if __name__ == '__main__':
    print dir(Animal)
    dog = Animal('dog', 2)
    print dir(dog)
    print dir(Plant)
    '''
    dog.cry()
    Animal.print_args(1, 2, a='b')
    print Animal.incr
    cat = Animal('cat', 1)
    
    print 'Class', Animal.incr, Animal.getIncr()
    print 'dog', dog.incr, dog.getIncr()
    print 'cat', cat.incr, cat.getIncr()

    Animal.incr = 10
    print 'Class', Animal.incr, Animal.getIncr()
    print 'dog', dog.incr, dog.getIncr()
    print 'cat', cat.incr, cat.getIncr()
    dog.incr = 5
    print 'Class', Animal.incr, Animal.getIncr()
    print 'dog', dog.incr, dog.getIncr()
    print 'cat', cat.incr, cat.getIncr()
    #print dog.name
    #dog.run()
    #cat.run()
    print dog.age
    print type(dog)
    print type(cat)
    print isinstance(dog, Animal)
    print isinstance(dog, Plant)
    '''
