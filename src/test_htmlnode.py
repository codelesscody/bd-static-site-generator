import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("div", "This is a div")
        node2 = HTMLNode("div", "This is a div")
        self.assertEqual(node, node2)

    def test_neq(self):
        node = HTMLNode("div", "This is a div")
        node2 = HTMLNode("span", "This is a div")
        self.assertNotEqual(node, node2)
    
    def testprops_to_html(self):
        node = HTMLNode("a", "This is a link", [], {"href": "https://www.example.com", "class": "link"})
        self.assertEqual(node.props_to_html(), 'href="https://www.example.com" class="link"')

if __name__ == "__main__":
    unittest.main()