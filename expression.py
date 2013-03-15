from namespace import *

class Expression(object):
    
    def __init__(self, namespace):
        self.namespace = namespace
        
    def run(self):
        pass
    
class Assignment(Expression):
    
    def __init__(self, namespace, var, expr):
        Expression.__init__(self, namespace)
        self.var = var
        self.expr = expr 