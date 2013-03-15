class NameExists(Exception):
    pass

class NamedObject(object):
    def __init__(self, name, namespace = None):
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
    def __init__(self, name, namespace = None):
        NamedObject.__init__(self, name, namespace)
        self.names = {}
        
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
    
