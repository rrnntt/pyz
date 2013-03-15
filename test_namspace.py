import unittest
from namespace import *

class TestNamespace(unittest.TestCase):
    
    def test_Namespace(self):
        ns = Namespace('global')
        ns.add_name('local','stuff')
        self.assertTrue('local' in ns)
        self.assertRaises(NameExists, lambda : ns.add_name('local','other stuff'))
        
    def test_nested_namespaces(self):
        ns = Namespace('global')
        ns1 = Namespace('local', ns)
        ns2 = Namespace('local1', ns1)
        self.assertEqual(ns.full_name(), 'global')
        self.assertEqual(ns1.full_name(), 'global.local')
        self.assertEqual(ns2.full_name(), 'global.local.local1')
        self.assertTrue( ns1.name in ns )
        self.assertFalse( ns1 in ns )
        self.assertFalse( ns2.name in ns )
        self.assertFalse( ns2 in ns )
        self.assertTrue( ns.contains(ns1) )
        self.assertFalse( ns.contains(ns2) )
        self.assertTrue( ns1.contains(ns2) )
        self.assertEqual( ns['local'], ns1 )
        self.assertEqual( ns1['local1'], ns2 )
        self.assertRaises( KeyError, lambda : ns['local1'] )
