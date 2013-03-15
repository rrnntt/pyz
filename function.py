import sympy
from namespace import *
from variable import *

class Function(object):
    
    def __init__(self):
        self.args = {}
    
    def declarg(self, name, Type, value = None):
        """Declare a function argument.
        
        Args:
            name (str): name of the argument,
            Type (?): type of the argument,
            value (?): initial vlaue (optional)
        """