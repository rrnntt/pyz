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
        if ival2.contains(0):
            raise DivisionByZero()
        # rubbish
        bounds = [ival1.start / ival2.start,
                  ival1.start / ival2.end,
                  ival1.end / ival2.start,
                  ival1.end / ival2.end
                  ]
        start = min(bounds)
        end = max(bounds)
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
    
    def __mul__(self, other):
        return self._bin_operation(other, self._mul_intervals)
    
    def __or__(self, other):
        dom = self.domain | other.domain
        return Double( dom )
    