import sympy
from namespace import *
from Types import *

class Variable(NamedObject):
    def __init__(self, namespace, name, typ = None, value = None):
        """Declare a variable.
        
        Args:
            name (str): name of the argument,
            typ  (Type): type of the argument,
            value (?): initial vlaue (optional)
            namespace (Namespace): the namespace the variable belongs to.
        """
        if isinstance( namespace, sympy.Basic ):
            NamedObject.__init__(self, None)
            self.var = namespace
            self.typ = name
        else:
            self.var = sympy.Symbol( name )
            self.typ = typ
            NamedObject.__init__(self, name, namespace)

    def __str__(self):
        if self.name != None:
            return 'var ' + self.full_name() + ': ' + str(self.typ)
        else:
            return 'temp: ' + str(self.var)
    
    def __add__(self, other):
        if isinstance( other, Variable ):
            typ = self.typ + other.typ 
            var = self.var + other.var
        else:
            var, typ = self.typ.make_var(other)
            var = self.var + var
            typ = self.typ + typ 
        return Variable(var, typ)

    def __radd__(self, other):
        var, typ = self.typ.make_var(other)
        var += self.var
        typ += self.typ 
        return Variable(var, typ)
        
    def __sub__(self, other):
        if isinstance( other, Variable ):
            typ = self.typ - other.typ 
            var = self.var - other.var
        else:
            var, typ = self.typ.make_var(other)
            var = self.var - var
            typ = self.typ - typ 
        return Variable(var, typ)

    def __rsub__(self, other):
        var, typ = self.typ.make_var(other)
        var -= self.var
        typ -= self.typ 
        return Variable(var, typ)

    def __mul__(self, other):
        if isinstance( other, Variable ):
            typ = self.typ * other.typ 
            var = self.var * other.var
        else:
            var, typ = self.typ.make_var(other)
            var = self.var * var
            typ = self.typ * typ 
        return Variable(var, typ)

    def __rmul__(self, other):
        var, typ = self.typ.make_var(other)
        var *= self.var
        typ *= self.typ 
        return Variable(var, typ)

    def __div__(self, other):
        if isinstance( other, Variable ):
            typ = self.typ / other.typ 
            var = self.var / other.var
        else:
            var, typ = self.typ.make_var(other)
            var = self.var / var
            typ = self.typ / typ 
        return Variable(var, typ)

    def __rdiv__(self, other):
        var, typ = self.typ.make_var(other)
        var /= self.var
        typ /= self.typ 
        return Variable(var, typ)

    def __pow__(self, other):
        if isinstance( other, Variable ):
            typ = self.typ ** other.typ 
            var = self.var ** other.var
        else:
            var, typ = self.typ.make_var(other)
            var = self.var ** var
            typ = self.typ ** typ 
        return Variable(var, typ)

    def __rpow__(self, other):
        var, typ = self.typ.make_var(other)
        var **= self.var
        typ **= self.typ 
        return Variable(var, typ)
                