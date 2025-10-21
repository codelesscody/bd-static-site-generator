from textnode import TextNode, TextType
import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type == TextType.TEXT and delimiter in node.text:
            parts = node.text.split(delimiter)
            # if there are not an even number of delimiters or zero, raise an error
            if len(parts) % 2 == 0:
                raise ValueError(f"Unmatched delimiter: {delimiter}")
            for i, part in enumerate(parts):
                if i % 2 == 0:
                    new_nodes.append(TextNode(part, TextType.TEXT))
                else:
                    new_nodes.append(TextNode(part, text_type))
        else:
            new_nodes.append(node)
    return new_nodes

# takes raw markdown text and returns a list of tuples. Each tuple should contain the alt text and the URL of any markdown images.
def extract_markdown_images(text):
    pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches

# extracts markdown links instead of images. It should return tuples of anchor text and URLs.
def extract_markdown_links(text):
    pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches


# [
#     TextNode("This is text with a link ", TextType.TEXT),
#     TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
#     TextNode(" and ", TextType.TEXT),
#     TextNode(
#         "to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"
#     ),
# ]
def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type == TextType.TEXT:
            matches = extract_markdown_images(node.text)
            if matches:
                last_index = 0
                for alt_text, url in matches:
                    start_index = node.text.find(f"![{alt_text}]({url})", last_index)
                    if start_index > last_index:
                        new_nodes.append(TextNode(node.text[last_index:start_index], TextType.TEXT))
                    new_nodes.append(TextNode(alt_text, TextType.IMAGE, url))
                    last_index = start_index + len(f"![{alt_text}]({url})")
                if last_index < len(node.text):
                    new_nodes.append(TextNode(node.text[last_index:], TextType.TEXT))
            else:
                new_nodes.append(node)
        else:
            new_nodes.append(node)
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type == TextType.TEXT:
            matches = extract_markdown_links(node.text)
            if matches:
                last_index = 0
                for anchor_text, url in matches:
                    start_index = node.text.find(f"[{anchor_text}]({url})", last_index)
                    if start_index > last_index:
                        new_nodes.append(TextNode(node.text[last_index:start_index], TextType.TEXT))
                    new_nodes.append(TextNode(anchor_text, TextType.LINK, url))
                    last_index = start_index + len(f"[{anchor_text}]({url})")
                if last_index < len(node.text):
                    new_nodes.append(TextNode(node.text[last_index:], TextType.TEXT))
            else:
                new_nodes.append(node)
        else:
            new_nodes.append(node)
    return new_nodes

# return a list of nodes given a raw text input, where each text is a TextNode of the appropriate type.
def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes
