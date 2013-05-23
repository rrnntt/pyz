from sympy.core import relational
from namespace import NamedObject, Namespace
from variable import Variable
#from context import *

class Function(NamedObject):
    
    def __init__(self,name,namespace):
        NamedObject.__init__(self, name, namespace)
        self.args = []
        self.ret = None
        self.local_namespace = Namespace(self.name)
        self.post_cond = True 
        
    def declare(self):
        pass
    
    def define(self):
        pass
    
    def run(self, context):
        
        pass
    
    def arg(self, name, typ, value = None):
        """Declare a function argument.
        
        Args:
            name (str): name of the argument,
            typ (?): type of the argument,
            value (?): initial vlaue (optional)
        """
        x = Variable(self.local_namespace, name, typ)
        self.args.append(x)
        
    def retType(self, typ):
        self.ret = typ

    def post(self, cond):
        if isinstance(cond,bool) or isinstance( cond, relational.Relational ):
            self.post_cond = cond
        