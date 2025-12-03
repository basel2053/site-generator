from textnode import TextType

class HTMLNode():
    def __init__(self,tag=None,value=None,children=None,props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    def to_html(self):
        raise NotImplementedError()
    def props_to_html(self):
        if self.props is None:
            return ""
        output =""
        for key,value in self.props.items():
            output += f' {key}="{value}"'
        return output
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

class LeafNode(HTMLNode):
    def __init__(self,tag,value,props=None):
        super().__init__(tag,value,None,props)
    def to_html(self):
        if self.value is None:
            raise ValueError("All leaf nodes msut have a value")
        if self.tag is None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

class ParentNode(HTMLNode):
    def __init__(self,tag,children,props=None):
        super().__init__(tag,None,children,props)
    def to_html(self):
        if self.tag is None:
            raise ValueError("All parent nodes msut have a tag")
        if self.children is None:
            raise ValueError("All parent nodes msut have children")
        children_text=""
        for child in self.children:
            children_text += child.to_html()
        return f"<{self.tag}{self.props_to_html()}>{children_text}</{self.tag}>"


def text_node_to_html_node(text_node):
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(tag=None, value=text_node.text)
        case TextType.BOLD:
            return LeafNode(tag="b", value=text_node.text)
        case TextType.ITALIC:
            return LeafNode(tag="i", value=text_node.text)
        case TextType.CODE:
            return LeafNode(tag="code", value=text_node.text)
        case TextType.LINK:
            return LeafNode(tag="a", value=text_node.text,props={"href":text_node.link})
        case TextType.IMAGE:
            return LeafNode(tag="img", value="",props={"src":text_node.link,"alt":text_node.text})
        case _:
            raise Exception("text_node must be an instance of TextType")



