import unittest
from variable import *

def getit(i):
    return sympy.Rational(i,3)

class TestVariable(unittest.TestCase):
    
    def test_add(self):
        
        X = Variable(None, 'x', Double(1,2))
        Y = Variable(None, 'y', Double(3,4))
        
        self.assertEqual( str(X), 'var x: Double([1, 2])')
        self.assertEqual( str(Y), 'var y: Double([3, 4])')
        d = X + Y
        self.assertEqual( str(d), 'temp: x + y')
        self.assertEqual( type(d), Variable )
        self.assertTrue( isinstance(d.var, sympy.Basic ) )
        self.assertEqual( str(d.typ), 'Double([4, 6])')

        d = X + 1
        self.assertEqual( str(d), 'temp: x + 1')
        self.assertEqual( type(d), Variable )
        self.assertTrue( isinstance(d.var, sympy.Basic ) )
        self.assertEqual( str(d.typ), 'Double([2, 3])')
        
        d = 1 + X
        self.assertEqual( str(d), 'temp: x + 1')
        self.assertEqual( type(d), Variable )
        self.assertTrue( isinstance(d.var, sympy.Basic ) )
        self.assertEqual( str(d.typ), 'Double([2, 3])')
        
        d = X + sympy.pi
        self.assertEqual( str(d), 'temp: x + 3.14159265358979')
        self.assertEqual( type(d), Variable )
        self.assertTrue( isinstance(d.var, sympy.Basic ) )
        self.assertEqual( str(d.typ), 'Double([4.14159265358979, 5.14159265358979])')
        
        d = sympy.pi + X
        self.assertEqual( str(d), 'temp: x + 3.14159265358979')
        self.assertEqual( type(d), Variable )
        self.assertTrue( isinstance(d.var, sympy.Basic ) )
        self.assertEqual( str(d.typ), 'Double([4.14159265358979, 5.14159265358979])')
        
        d = X + 2*sympy.pi
        self.assertEqual( str(d), 'temp: x + 6.28318530717959')
        self.assertEqual( type(d), Variable )
        self.assertTrue( isinstance(d.var, sympy.Basic ) )
        self.assertEqual( str(d.typ), 'Double([7.28318530717959, 8.28318530717959])')
        
        d = X + 2*sympy.pi + Y
        self.assertEqual( str(d), 'temp: x + y + 6.28318530717959')
        self.assertEqual( type(d), Variable )
        self.assertTrue( isinstance(d.var, sympy.Basic ) )
        self.assertEqual( str(d.typ), 'Double([10.2831853071796, 12.2831853071796])')

    def test_sub(self):
        
        X = Variable(None, 'x', Double(1,2))
        Y = Variable(None, 'y', Double(3,4))
        
        self.assertEqual( str(X), 'var x: Double([1, 2])')
        self.assertEqual( str(Y), 'var y: Double([3, 4])')
        d = X - Y
        self.assertEqual( str(d), 'temp: x - y')
        self.assertEqual( type(d), Variable )
        self.assertTrue( isinstance(d.var, sympy.Basic ) )
        self.assertEqual( str(d.typ), 'Double([-3, -1])')

        d = X - 1
        self.assertEqual( str(d), 'temp: x - 1')
        self.assertEqual( type(d), Variable )
        self.assertTrue( isinstance(d.var, sympy.Basic ) )
        self.assertEqual( str(d.typ), 'Double([0, 1])')
        
        d = 1 - X
        self.assertEqual( str(d), 'temp: -x + 1')
        self.assertEqual( type(d), Variable )
        self.assertTrue( isinstance(d.var, sympy.Basic ) )
        self.assertEqual( str(d.typ), 'Double([-1, 0])')
        
        d = X - sympy.pi
        self.assertEqual( str(d), 'temp: x - 3.14159265358979')
        self.assertEqual( type(d), Variable )
        self.assertTrue( isinstance(d.var, sympy.Basic ) )
        self.assertEqual( str(d.typ), 'Double([-2.14159265358979, -1.14159265358979])')
        
        d = sympy.pi - X
        self.assertEqual( str(d), 'temp: -x + 3.14159265358979')
        self.assertEqual( type(d), Variable )
        self.assertTrue( isinstance(d.var, sympy.Basic ) )
        self.assertEqual( str(d.typ), 'Double([1.14159265358979, 2.14159265358979])')
        
        d = X - 2*sympy.pi
        self.assertEqual( str(d), 'temp: x - 6.28318530717959')
        self.assertEqual( type(d), Variable )
        self.assertTrue( isinstance(d.var, sympy.Basic ) )
        self.assertEqual( str(d.typ), 'Double([-5.28318530717959, -4.28318530717959])')
        
        d = X + 2*sympy.pi - Y
        self.assertEqual( str(d), 'temp: x - y + 6.28318530717959')
        self.assertEqual( type(d), Variable )
        self.assertTrue( isinstance(d.var, sympy.Basic ) )
        self.assertEqual( str(d.typ), 'Double([3.28318530717959, 5.28318530717959])')

    def test_pow(self):
        
        X = Variable(None, 'x', Double(1,2))
        Y = Variable(None, 'y', Double(3,4))
        
        d = X ** Y
        self.assertEqual( str(d), 'temp: x**y')
        self.assertEqual( type(d), Variable )
        self.assertTrue( isinstance(d.var, sympy.Basic ) )
        self.assertEqual( str(d.typ), 'Double([1, 16])')

        d = Y ** 2
        self.assertEqual( str(d), 'temp: y**2')
        self.assertEqual( type(d), Variable )
        self.assertTrue( isinstance(d.var, sympy.Basic ) )
        self.assertEqual( str(d.typ), 'Double([9, 16])')

        d = Y ** sympy.Rational(1,2)
        self.assertEqual( str(d), 'temp: y**0.5')
        self.assertEqual( type(d), Variable )
        self.assertTrue( isinstance(d.var, sympy.Basic ) )
        self.assertEqual( str(d.typ), 'Double([sqrt(3), 2])')

        d = Y ** (-0.3)
        self.assertEqual( str(d), 'temp: y**(-0.3)')
        self.assertEqual( type(d), Variable )
        self.assertTrue( isinstance(d.var, sympy.Basic ) )
        self.assertEqual( str(d.typ), 'Double([4**(-0.3), 3**(-0.3)])')

        d = (1.5) ** Y
        self.assertEqual( str(d), 'temp: 1.5**y')
        self.assertEqual( type(d), Variable )
        self.assertTrue( isinstance(d.var, sympy.Basic ) )
        self.assertEqual( str(d.typ), 'Double([3.375, 5.0625])')

        self.assertRaises(DoubleUnderflow, lambda : (-1.5) ** Y )
        