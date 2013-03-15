import unittest
import defaults
from Types import *

class TestTypes(unittest.TestCase):
    
    def test_Double(self):
        
        typ = Double()
        self.assertFalse( typ.const )
        typ = Double(const = True)
        self.assertTrue( typ.const )
        
        dt = Double(sympy.Interval(1,2))
        self.assertTrue(isinstance(dt.domain, sympy.Interval))
        self.assertEqual(dt.domain.start, 1)
        self.assertEqual(dt.domain.end, 2)

        dt = Double(sympy.Interval(1,2).union(sympy.Interval(3,4)))
        dom = dt.domain
        self.assertTrue(isinstance(dom, sympy.Union))
        
#        x = sympy.Symbol('x')
#        y = eval('1+2*x')
#        print type(x),y.args,str(x)
        
        d1 = Double(1,2)
        d2 = Double(3,4)
        d = d1 + d2
        self.assertTrue(isinstance(d.domain, sympy.Interval))
        self.assertEqual(d.domain.start, 4)
        self.assertEqual(d.domain.end, 6)
        self.assertEqual( str(d.domain), '[4, 6]')
        
        d1 = Double(1,2)
        d2 = Double(10,11)
        d =  d1 | d2
        dom = d.domain
        self.assertTrue(isinstance(dom, sympy.Union))
        self.assertEqual( str(dom), '[1, 2] U [10, 11]')
        dd = d + d1
        self.assertEqual( str(dd.domain), '[2, 4] U [11, 13]')
        dd = d - d1
        self.assertEqual( str(dd.domain), '[-1, 1] U [8, 10]')
        d -= d1
        self.assertEqual( str(dd.domain), '[-1, 1] U [8, 10]')
        
    def test_get_bounds(self):
        dom = sympy.Interval(1,2).union(sympy.Interval(3,4))
        bounds = get_bounds(dom)
        self.assertEqual( bounds, [1,2,3,4] )
        dom = sympy.Interval(1,2).union(sympy.Interval(3,4).union(sympy.Interval(10,11)))
        bounds = get_bounds(dom)
        self.assertEqual( bounds, [1, 2, 3, 4, 10, 11] )
        
    def test_Double_division(self):
        
        d1 = Double(1,2)
        d2 = Double(3,4)
        d = d1 / d2
        self.assertEqual( str(d.domain), '[1/4, 2/3]')

        d1 = Double(-1,2)
        d2 = Double(-4, -3)
        d = d1 / d2
        self.assertEqual( str(d.domain), '[-2/3, 1/3]')

        d1 = Double(1,2)
        d2 = Double(-1,1)
        self.assertRaises( DivisionByZero, lambda : d1 / d2 )
        
    def test_Double_pow(self):
        
        d1 = Double(1,2)
        d2 = Double(3,4)
        d = d1 ** d2
        self.assertEqual( str(d.domain), '[1, 16]')

        d1 = Double(0,200)
        d2 = Double(0,4)
        self.assertRaises( DoubleUnderflow, lambda : d1 ** d2 )
        