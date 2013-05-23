import unittest
from function import Function
from namespace import Namespace, NameExists
from Types import Double
import sympy



class TestFunction(unittest.TestCase):
    
    def test_Namespace(self):
        ns = Namespace('global')
        ns.add_name('local','stuff')
        self.assertTrue('local' in ns)
        self.assertRaises(NameExists, lambda : ns.add_name('local','other stuff'))
        
    def test_logic(self):
        x = sympy.Symbol('x')
        rel = x > 0
        print type(rel)
        print type( rel.subs(x,1) ), isinstance( rel, sympy.relational.Relational ) 

    def test_function(self):
        
        class MaxXY(Function):
            
            def declare(self):
                self.arg('x', Double)
                self.arg('y', Double)
    
        ns = Namespace('global')
        fun = MaxXY("maxxy", ns)
        fun.declare()
        
        print str(fun.args[0]),str(fun.args[1])
        