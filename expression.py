from namespace import *
from variable import *

class Expression(object):
    
    def __init__(self, namespace):
        self.namespace = namespace
        
    def run(self):
        pass
    
class Assignment(Expression):
    
    def __init__(self, namespace, var, expr):
        Expression.__init__(self, namespace)
        if var.name == None:
            raise Exception('Assignment to temporary variable (rvalue).')
        if type(var) != type(expr):
            raise Exception('Incompatible types in assignment.')
        self.var = var
        self.expr = expr 
        
    def run(self):
        self.var.typ = self.expr.typ
        