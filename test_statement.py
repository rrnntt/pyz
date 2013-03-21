import unittest
from statement import *
import copy


class TestStatement(unittest.TestCase):
    
    def test_assignment(self):
        ns = None
        ctx = Context(ns)
        x = Variable(ns, 'x', Double())
        y = Variable(ns, 'y', Double(1,2))
        self.assertEqual( str(x), 'var x: Double([-1.0e+300, 1.0e+300])' )
        self.assertEqual( str(y), 'var y: Double([1, 2])' )
        ass = Assignment(ctx, x, y)
        ass.run()
        self.assertEqual( str(x), 'var x: Double([1, 2])' )
        
        Assignment(ctx, y, 2*y).run()
        self.assertEqual( str(x), 'var x: Double([1, 2])' )
        self.assertEqual( str(y), 'var y: Double([2, 4])' )
        
    def test_logic(self):
        x = sympy.Symbol('x')
        rel = x > 0
        self.assertTrue( rel.subs(x,1) )
        self.assertFalse( rel.subs(x,-1) )
        self.assertFalse( rel.subs(x,0) )
        
    def test_copy(self):
        ns = Namespace('ns')
        y = Variable(ns, 'y', Double(1,2))
        y1 = copy.copy(y)
        y1.typ = Double(3,4)
        self.assertEqual( str(y), 'var ns.y: Double([1, 2])')
        self.assertEqual( str(y1), 'var ns.y: Double([3, 4])')
        self.assertTrue( ns.contains(y) )
        self.assertTrue( ns.contains(y1) )
        self.assertFalse( y == y1 )
        
    def test_block(self):
        ns = None
        ctx = Context(ns)
        x = Variable(ns, 'x', Double(1,2))
        y = Variable(ns, 'y', Double(3,4))
        
        
