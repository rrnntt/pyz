import sympy

class NameExists(Exception):
    pass

class NamedObject(object):
    def __init__(self, name, namespace = None):
        self.name = name
        if namespace != None:
            namespace.add_name( name, self )
        self.namespace = namespace

class Namespace(NamedObject):
    def __init__(self, name, namespace = None):
        NamedObject.__init__(self, name, namespace)
        self.names = {}
        
    def full_name(self):
        """Fully qualified namespace name."""
        if self.namespace != None:
            return self.namespace.full_name() + '.' + self.name
        else:
            return self.name
        
    def add_name(self, name, obj):
        if name in self.names:
            raise NameExists("Name " + name + " already exists in namespace " + self.full_name())
        self.names[name] = obj
        
    def contains(self, obj):
        return obj in self.names.itervalues()
        
    def __iter__(self):
        return iter(self.names)
    
    def __getitem__(self, name):
        return self.names[name]
    
class Variable(NamedObject):
    def __init__(self, name, typ, value = None, namespace = None):
        """Declare a variable.
        
        Args:
            name (str): name of the argument,
            typ  (?): type of the argument,
            value (?): initial vlaue (optional)
            namespace (Namespace): the namespace the variable belongs to.
        """
        NamedObject.__init__(self, name, namespace)
        self.name = name
        self.var = sympy.Symbol( name )
        self.typ = typ

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