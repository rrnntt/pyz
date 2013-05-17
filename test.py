import sympy
from sympy import Set, Interval, FiniteSet, oo, Rational, Tuple, S, Symbol, sin
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

Doubles = Interval(-1e300,1e300)
print Doubles
v = S(1e300)
print type(v),v,Doubles.contains(v)

print Doubles * Doubles

x = Symbol('x', real = True, bounded = True)

print ( Interval(x+2,100) | Interval(x+3,100) ).contains(x+4.0) & (x < 90)
print Interval(x+4.0,100) & Interval(x+3,100)

print x.is_bounded

print Interval(sin(x),100)

print (x < 1) & (x > 0)
