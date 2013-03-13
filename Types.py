import sympy

class Type(object):
    def __init__(self, const):
        self.const = const
        
default_const = False

class Double(Type):
    
    dmin = -1e300
    dmax = 1e300
    
    def __init__(self, start = -1e300, end = 1e300, const = default_const):
        Type.__init__(self, const)
        self.domain = sympy.Interval(start,end)
            
    def __str__(self):
        out = 'Double(' + str(self.domain)
        if self.const:
            out += ' const'
        return  out + ')'
    
    def _check_overflow(self, start, end):
        if start <= self.dmin:
            raise Exception('Double negative overflow')
        if end >= self.dmax:
            raise Exception('Double positive overflow')
    
    def __add__(self, other):
        start = self.domain.start + other.domain.start
        end = self.domain.end + other.domain.end
        self._check_overflow(start, end)
        return Double(start, end)
    
    def __sub__(self, other):
        start = self.domain.start - other.domain.end
        end = self.domain.end - other.domain.start
        self._check_overflow(start, end)
        return Double(start, end)
    
