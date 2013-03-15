import unittest
from function import *

class TestFunction(unittest.TestCase):
    
    def test_Namespace(self):
        ns = Namespace('global')
        ns.add_name('local','stuff')
        self.assertTrue('local' in ns)
        self.assertRaises(NameExists, lambda : ns.add_name('local','other stuff'))
        
