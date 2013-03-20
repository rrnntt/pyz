from namespace import *
from variable import *

class Statement(object):
    
    def __init__(self, namespace):
        self.namespace = namespace
        
    def run(self):
        self._run()
    
class Assignment(Statement):
    
    def __init__(self, namespace, var, expr):
        Statement.__init__(self, namespace)
        if var.name == None:
            raise Exception('Assignment to temporary variable (rvalue).')
        if type(var) != type(expr):
            raise Exception('Incompatible types in assignment.')
        self.var = var
        self.expr = expr 
        
    def _run(self):
        self.var.typ = self.expr.typ
        
class IfStatement(Statement):
    def __init__(self, namespace, clauses):
        Statement.__init__(self, namespace)
        self.clauses = clauses
        
    def _run(self):
        pass
        