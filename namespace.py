import re

class NameExists(Exception):
    pass

class EmptyName(Exception):
    pass

class InvalidName(Exception):
    pass

def isVariable(obj):
    return hasattr(obj,'var')

name_pattern = re.compile('[a-zA-Z]\w*')
def validate_name(name):
    if not re.match( name_pattern, name ):
        raise InvalidName( 'Invalid object name ' + name )

class NamedObject(object):
    """Any object with a name.
    
    Args:
        name (str): objects name. Cannot be empty.
        namespace (Namespace): If namespace is given this object will be attached to that namespace. 
    """
    def __init__(self, name, namespace = None):
        if name == None:
            self.name = None
            self.namespace = None
        else:
            # name cannot be empty
            if name == '':
                raise EmptyName( "NamedObject must have a non-empty name." )
            validate_name(name)
            self.name = name
            if namespace != None:
                namespace.add_name( name, self )
            self.namespace = namespace

    def full_name(self):
        """Fully qualified namespace name."""
        if self.namespace != None:
            return self.namespace.full_name() + '.' + self.name
        else:
            return self.name
        
class Namespace(NamedObject):
    """A collection of named objects."""
    def __init__(self, name, namespace = None):
        NamedObject.__init__(self, name, namespace)
        self.names = {}
        
    def add_name(self, name, obj):
        if name in self.names:
            raise NameExists("Name " + name + " already exists in namespace " + self.full_name())
        if isVariable(obj):
            self.names[name] = obj.var
        else:
            self.names[name] = obj
        
    def contains(self, obj):
        if isVariable(obj):
            return obj.var in self.names.itervalues()
        return obj in self.names.itervalues()
        
    def __iter__(self):
        return iter(self.names)
    
    def __getitem__(self, name):
        return self.names[name]
    
