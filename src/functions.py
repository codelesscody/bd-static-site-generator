from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if isinstance(node, TextNode.TEXT):
            parts = node.text.split(delimiter)
            # if there are not an even number of delimiters or zero, raise an error
            if len(parts) % 2 == 0 or len(parts) == 0:
                raise ValueError(f"Unmatched delimiter: {delimiter}")
            for i, part in enumerate(parts):
                if i % 2 == 0:
                    new_nodes.append(TextNode(part, TextType.TEXT))
                else:
                    new_nodes.append(TextNode(part, text_type))
        else:
            new_nodes.append(node)
    return new_nodes