import sympy

class Type(object):
    def __init__(self, const):
        self.const = const
        
    def _combine_const(self, other):
        return self.const or other.const
        
default_const = False

class Double(Type):
    
    dmin = -1e300
    dmax = 1e300
    
    def __init__(self, start = -1e300, end = 1e300, const = default_const):
        Type.__init__(self, const)
        if isinstance( start, sympy.Set ):
            self.domain = start
        else:
            self.domain = sympy.Interval(start,end)
            
    def __str__(self):
        out = 'Double(' + str(self.domain)
        if self.const:
            out += ' const'
        return  out + ')'
    
    def _check_overflow(self, dom ):
        if isinstance( dom, sympy.Interval ):
            if dom.start <= self.dmin:
                raise Exception('Double negative overflow')
            if dom.end >= self.dmax:
                raise Exception('Double positive overflow')
        else:
            raise Exception("Domain incompatible with Double: " + str(dom))
        
    def _add_intervals(self, ival1, ival2):
        """Return domain of addition of two doubles lying in intervals ival1 and ival2."""
        start = ival1.start + ival2.start
        end = ival1.end + ival2.end
        ival = sympy.Interval(start, end)
        self._check_overflow( ival )
        return ival
    
    def _sub_intervals(self, ival1, ival2):
        """Return domain of subtraction of two doubles lying in intervals ival1 and ival2."""
        start = ival1.start - ival2.end
        end = ival1.end - ival2.start
        ival = sympy.Interval(start, end)
        self._check_overflow( ival )
        return ival
    
    def _bin_operation(self, other, op):
        dom1 = self.domain
        dom2 = other.domain
        dom = sympy.EmptySet()
        if isinstance( dom1, sympy.Union ):
            if isinstance( dom2, sympy.Union ):
                for d1 in dom1.args:
                    for d2 in dom2.args:
                        dom |= op( d1, d2 )
            else:
                for d1 in dom1.args:
                    dom |= op( d1, dom2 )
        elif isinstance( dom2, sympy.Union ):
            for d2 in dom2.args:
                dom |= op( dom1, d2 )
        else:
            dom = op(dom1, dom2)
        return Double( dom )
    
    
    def __add__(self, other):
        return self._bin_operation(other, self._add_intervals)
    
    def __sub__(self, other):
        return self._bin_operation(other, self._sub_intervals)
    
    def __or__(self, other):
        dom = self.domain | other.domain
        return Double( dom )
    