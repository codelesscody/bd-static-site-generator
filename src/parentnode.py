from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag: str, children: list, props: dict = None):
        super().__init__(tag, None, children=children, props=props)  # Parent nodes have no value, and ONLY have children

    def to_html(self):
        if not self.tag:
            raise ValueError("Tag cannot be empty for ParentNode.")
        if self.children is None:
            raise ValueError("Children cannot be None for ParentNode.")
        props_str = self.props_to_html() if self.props else ""
        opening_tag = f"<{self.tag} {props_str}".strip() + ">"
        closing_tag = f"</{self.tag}>"
        children_html = "".join(child.to_html() for child in self.children)
        return f"{opening_tag}{children_html}{closing_tag}"
