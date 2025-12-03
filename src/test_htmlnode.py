import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode,text_node_to_html_node
from textnode import TextNode, TextType

class TestHTMLNode(unittest.TestCase):
    def test_props(self):
        html = HTMLNode(tag="div",props={"id":"test","class":"test"})
        self.assertEqual(html.props_to_html(),''' id="test" class="test"''')
    def test_to_html(self):
        html = HTMLNode(tag="p",value="text")
        self.assertRaises(NotImplementedError,html.to_html)
    def test_repr(self):
        html = HTMLNode(tag="p",value="text")
        self.assertEqual(html.__repr__(),"HTMLNode(p, text, None, None)")

class TestLeafNode(unittest.TestCase):
    def test_to_html(self):
        html = LeafNode(tag="p",value="dummy text")
        self.assertEqual(html.to_html(),"<p>dummy text</p>")
    def test_to_html_no_tag(self):
        html = LeafNode(tag=None,value="text")
        self.assertEqual(html.to_html(),"text")
    def test_to_html_no_value(self):
        html = LeafNode(tag="p",value=None)
        self.assertRaises(ValueError,html.to_html)

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

class Testtext_node_to_html_node(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
