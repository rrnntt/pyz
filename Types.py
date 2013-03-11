from sympy import Set, Interval, FiniteSet, oo, Rational, Tuple, S, EmptySet
from sympy.sets.fancysets import Reals

Doubles = Interval(-1e300,1e300)

class Double(Set):
    
    dmin = -1e300
    dmax = 1e300
    
    def __init__(self, start = -1e300, end = 1e300):
        self.domain = Interval(start,end)
            
    def __str__(self):
        return 'Double(' + str(self.domain) + ')'
    
    def __add__(self, other):
        start = self.domain.start + other.domain.start
        end = self.domain.end + other.domain.end
        if start <= self.dmin:
            raise Exception('Double negative overflow')
        if end >= self.dmax:
            raise Exception('Double positive overflow')
        return Double(start, end)

d = Double(1,2)
print d+Double()
