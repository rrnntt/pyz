import unittest
from Types import *

class TestTypes(unittest.TestCase):
    
    def test_Double(self):
        
        typ = Double()
        self.assertFalse( typ.const )
        typ = Double(const = True)
        self.assertTrue( typ.const )
        
        x = sympy.Symbol('x')
        y = eval('2*x+1')
        print type(x),y.args,str(x)
        
        d1 = Double(1,2)
        d2 = Double(3,4)
        d1 += d2
        print d1
    