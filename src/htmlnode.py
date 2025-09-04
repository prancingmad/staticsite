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