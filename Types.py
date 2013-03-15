import sympy
import defaults

class Type(object):
    def __init__(self, const):
        self.const = const
        
    def _combine_const(self, other):
        return self.const or other.const
        
class DivisionByZero(Exception):
    pass

class DoubleOverflow(Exception):
    pass

class DoubleUnderflow(Exception):
    pass

def get_bounds( dom ):
    """Get a list of all interval bounds that can be found in dom"""
    bounds = []
    if isinstance( dom, sympy.Union ):
        for d in dom.args:
            bounds += get_bounds(d)
    elif isinstance( dom, sympy.Interval ):
        bounds.append( dom.start )
        bounds.append( dom.end )
    return bounds
    

class Double(Type):
    
    def __init__(self, start = -1e300, end = 1e300, const = defaults.const):
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
        if defaults.DoublesInterval | dom != defaults.DoublesInterval:
            raise DoubleOverflow('Double negative overflow')
        
    def _check_underflow(self, dom ):        
        if defaults.DoublesUndeflowInterval & dom != sympy.EmptySet():
            raise DoubleUnderflow(str(dom))
        
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
    
    def _mul_intervals(self, ival1, ival2):
        """Return domain of multiplication of two doubles lying in intervals ival1 and ival2."""
        start = ival1.start * ival2.start
        end = ival1.end * ival2.end
        ival = sympy.Interval(start, end)
        self._check_overflow( ival )
        return ival
    
    def _div_intervals(self, ival1, ival2):
        """Return domain of division of two doubles lying in intervals ival1 and ival2."""
        try:
            self._check_underflow(ival2)
        except:
            raise DivisionByZero()
        # because we checked for underflow ival2 excludes the area around the zero 
        # and it is not a union because ival2 is an interval
        bounds = [ival1.start / ival2.start,
                  ival1.start / ival2.end,
                  ival1.end / ival2.start,
                  ival1.end / ival2.end
                  ]
        start = min(bounds)
        end = max(bounds)
        ival = sympy.Interval(start, end)
        self._check_overflow( ival )
        #self._check_underflow( ival )
        return ival
    
    def _pow_intervals(self, ival1, ival2):
        """Return domain of power of two doubles lying in intervals ival1 and ival2."""
        if (sympy.Interval(-sympy.oo, 0) | defaults.DoublesUndeflowInterval) & ival1 != sympy.EmptySet(): 
            raise DoubleUnderflow()
        start = ival1.start ** ival2.start
        end = ival1.end ** ival2.end
        if start < end:
            ival = sympy.Interval(start, end)
        else:
            ival = sympy.Interval(end, start)
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
    
    def __mul__(self, other):
        return self._bin_operation(other, self._mul_intervals)
    
    def __div__(self, other):
        return self._bin_operation(other, self._div_intervals)
    
    def __pow__(self, other):
        return self._bin_operation(other, self._pow_intervals)
    
    def __or__(self, other):
        dom = self.domain | other.domain
        return Double( dom )
    