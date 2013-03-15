import unittest
from expression import *


class TestExpression(unittest.TestCase):
    
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
        