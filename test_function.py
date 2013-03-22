import unittest
from function import *

class TestFunction(unittest.TestCase):
    
    def test_Namespace(self):
        ns = Namespace('global')
        ns.add_name('local','stuff')
        self.assertTrue('local' in ns)
        self.assertRaises(NameExists, lambda : ns.add_name('local','other stuff'))
        
    def test_function(self):
        pass
    
    def test_logic(self):
        x = sympy.Symbol('x')
        rel = x > 0
        print type(rel)
        print type( rel.subs(x,1) ), isinstance( rel, relational.Relational ) 
    