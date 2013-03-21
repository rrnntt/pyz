from namespace import *
from variable import *
from context import *
import copy

class Statement(object):
    
    def __init__(self, context):
        self.context = context
        
    def setContext(self, context):
        self.context = context
        
    def run(self):
        if self.context == None:
            raise Exception("Context is undefined in "+str(self.__class__))
        self._run()
    
class Assignment(Statement):
    
    def __init__(self, context, var, expr):
        Statement.__init__(self, context)
        if var.name == None:
            raise Exception('Assignment to temporary variable (rvalue).')
        if type(var) != type(expr):
            raise Exception('Incompatible types in assignment.')
        self.var = var
        self.expr = expr 
        
    def _run(self):
        self.var.typ = self.expr.typ
        
class IfStatement(Statement):
    def __init__(self, context, clauses):
        Statement.__init__(self, context)
        self.clauses = clauses
        for clause in clauses:
            clause.context = copy.copy(clause.context)
        
    def _run(self):
        pass
        
        
class BlockStatement(Statement):
    def __init__(self, context, statements):
        Statement.__init__(self, context)
        self.statements = statements
    
    def _run(self):
        for s in self.statements:
            s.run()
