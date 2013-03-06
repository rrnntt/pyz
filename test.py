import sympy
from sympy import Set, Interval, FiniteSet, oo, Rational, Tuple
from sympy.sets.fancysets import Reals

class String(sympy.Atom):
    def __init__(self, s = None):
        if s == None:
            self.data = ''
        else:
            self.data = str(s)            

    def __str__(self):
        return self.data
    
    def __add__(self, other):
        if isinstance(other, String):
            return self.__class__(self.data + other.data)
        else:
            return self.__class__(self.data + str(other))
    
    
s = String(Rational(1,2))
print s
hello = String('Hello')
world = String(' world!')

f = FiniteSet(s, hello)

print f

for a in f:
    print a, isinstance(a,String)
    
    
print hello + world
print hello + ' ' + Rational(3,4) 

t = Tuple(hello, f)
print t
print t[0]
