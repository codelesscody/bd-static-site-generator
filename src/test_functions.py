from functions import split_nodes_delimiter, extract_markdown_images, split_nodes_image, text_to_textnodes
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

    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_text_to_textnodes(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and an image ![alt text](https://i.imgur.com/zjjcJKZ.png)"
        nodes = [
            TextNode("This is text with a link ", TextType.TEXT),
            TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
            TextNode(" and an image ", TextType.TEXT),
            TextNode("alt text", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
        ]
        result_nodes = text_to_textnodes(text)
        self.assertListEqual(nodes, result_nodes)