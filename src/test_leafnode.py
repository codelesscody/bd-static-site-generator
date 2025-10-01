import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    
    def test_leaf_to_html_a_with_props(self):
        node = LeafNode("a", "Click here", {"href": "https://www.example.com", "class": "link"})
        self.assertEqual(node.to_html(), '<a href="https://www.example.com" class="link">Click here</a>')
    
    def test_eq(self):
        node = LeafNode("p", "Hello, world!")
        node2 = LeafNode("p", "Hello, world!")
        self.assertEqual(node, node2)
    
    def test_neq(self):
        node = LeafNode("p", "Hello, world!")
        node2 = LeafNode("p", "Hello, everyone!")
        self.assertNotEqual(node, node2)

