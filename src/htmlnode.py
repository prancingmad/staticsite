# python
class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if not self.props:
            return ""
        out = ""
        for k in sorted(self.props):
            v = self.props[k]
            out += f' {k}="{v}"'
        return out

    def __repr__(self):
        kids = len(self.children) if self.children else 0
        val = self.value if self.value is None or len(str(self.value)) <= 30 else str(self.value)[:27] + "..."
        return f"HTMLNode(tag={self.tag!r}, value={val!r}, children={kids}, props={self.props!r})"

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        if value is None:
            raise ValueError("LeafNode requires a non-None value")
        super().__init__(tag=tag, value=value, children=None, props=props)

    def to_html(self):
        if self.value is None:
            raise ValueError("LeafNode must have a value")
        if self.tag is None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        if tag is None:
            raise ValueError("ParentNode requires a tag")
        if children is None or len(children) == 0:
            raise ValueError("ParentNode requires at least one child")
        super().__init__(tag=tag, value=None, children=children, props=props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("ParentNode must have a tag")
        if not self.children:
            raise ValueError("ParentNode must have children")

        # Recursively render all children
        inner_html = "".join(child.to_html() for child in self.children)
        return f"<{self.tag}{self.props_to_html()}>{inner_html}</{self.tag}>"