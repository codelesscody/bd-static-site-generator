from functions import split_nodes_delimiter
from textnode import TextNode, TextType
import unittest

class TestFunctions(unittest.TestCase):
    def test_split_nodes_delimiter(self):
        old_nodes = [
            TextNode("This is a *bold* text", TextType.TEXT),
            TextNode("This is a normal text", TextType.TEXT),
            TextNode("This is an _italic_ text", TextType.TEXT),
        ]
        new_nodes = split_nodes_delimiter(old_nodes, "*", TextType.BOLD)
        new_nodes = split_nodes_delimiter(new_nodes, "_", TextType.ITALIC)
        expected_nodes = [
            TextNode("This is a ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" text", TextType.TEXT),
            TextNode("This is a normal text", TextType.TEXT),
            TextNode("This is an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" text", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, expected_nodes)

    def test_split_nodes_delimiter_unmatched(self):
        old_nodes = [
            TextNode("This is a *bold text", TextType.TEXT),
        ]
        with self.assertRaises(ValueError):
            split_nodes_delimiter(old_nodes, "*", TextType.BOLD)