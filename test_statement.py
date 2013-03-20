import unittest
from statement import *
import copy


class TestStatement(unittest.TestCase):
    
    def test_assignment(self):
        ns = None
        x = Variable(ns, 'x', Double())
        y = Variable(ns, 'y', Double(1,2))
        self.assertEqual( str(x), 'var x: Double([-1.0e+300, 1.0e+300])' )
        self.assertEqual( str(y), 'var y: Double([1, 2])' )
        ass = Assignment(ns, x, y)
        ass.run()
        self.assertEqual( str(x), 'var x: Double([1, 2])' )
        
        Assignment(ns, y, 2*y).run()
        self.assertEqual( str(x), 'var x: Double([1, 2])' )
        self.assertEqual( str(y), 'var y: Double([2, 4])' )
        
    def test_logic(self):
        x = sympy.Symbol('x')
        rel = x > 0
        print rel.subs(x,1), type(rel)
        
    def test_copy(self):
        ns = Namespace('')
        y = Variable(ns, 'y', Double(1,2))
        y1 = copy.copy(y)
        y1.typ = Double(3,4)
        print y, ns.contains(y)
        print y1, ns.contains(y1)
        print hasattr(y,'var'), y == y1
        
        
