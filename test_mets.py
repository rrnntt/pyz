
class Meta(type):
    def __new__(cls, name, bases, dct):
        #dct['hi'] = 'hello'
        return super(Meta, cls).__new__(cls, name, bases, dct)
    
    def __init__(cls, name, bases, dct):
        super(Meta, cls).__init__(name, bases, dct)
        cls.hi = 'hello world!'
        print 'dct',dct
        
class Class(object):
    __metaclass__ = Meta
    stuff = 0
    def __init__(self):
        self.numb = 10
        
    def tst(self):
        print 'tst'
    
    
    
c = Class()
c.stuff = 1
print dir(c)
c1 = Class()
print c1.stuff
print c.stuff, c.hi
c.hi = 'OK'
print c1.hi, c.hi
print Class.hi
print Class.stuff
#print Class.numb doesn't work

class DBInterfaceMeta(type):
    # we use __init__ rather than __new__ here because we want
    # to modify attributes of the class *after* they have been
    # created
    def __init__(cls, name, bases, dct):
        if not hasattr(cls, 'registry'):
            # this is the base class.  Create an empty registry
            cls.registry = {}
        else:
            # this is a derived class.  Add cls to the registry
            interface_id = name.lower()
            cls.registry[interface_id] = cls
            
        super(DBInterfaceMeta, cls).__init__(name, bases, dct)
        
class DBInterface(object):
    __metaclass__ = DBInterfaceMeta
    
print(DBInterface.registry)

class FirstInterface(DBInterface):
    pass

class SecondInterface(DBInterface):
    pass

class SecondInterfaceModified(SecondInterface):
    pass
    
print(DBInterface.registry)

fi = FirstInterface()

print(DBInterface.registry)

si = SecondInterface()
si.registry = {}

print(DBInterface.registry)

