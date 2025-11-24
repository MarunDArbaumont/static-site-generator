import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_eq_tag(self):
        node = HTMLNode("h1")
        node2 = HTMLNode("h1")
        self.assertEqual(node, node2)

    def test_diff_tag(self):
        node = HTMLNode("h1")
        node2 = HTMLNode("p")
        self.assertNotEqual(node, node2)

    def test_eq_value(self):
        node = HTMLNode(tag=None, value="This is a header")
        node2 = HTMLNode(tag=None, value="This is a header")
        self.assertEqual(node, node2)
    
    def test_diff_value(self):
        node = HTMLNode(tag=None, value="This is a header")
        node2 = HTMLNode(tag=None, value=None)
        self.assertNotEqual(node, node2)

    def test_eq_children(self):
        node = HTMLNode(tag=None, value=None, children=[HTMLNode("b", "this text is bold")])
        node2 = HTMLNode(tag=None, value=None, children=[HTMLNode("b", "this text is bold")])
        self.assertEqual(node, node2)

    def test_diff_children(self):
        node = HTMLNode(tag=None, value=None, children=[HTMLNode("b", "this text is bold")])
        node2 = HTMLNode(tag=None, value=None, children=None)
        self.assertNotEqual(node, node2)
    
    def test_eq_props(self):
        node = HTMLNode(tag=None, value=None, children=None, props={"href": "https://www.google.com", "target": "_blank"})
        node2 = HTMLNode(tag=None, value=None, children=None, props={"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node, node2)

    def test_diff_props(self):
        node = HTMLNode(tag=None, value=None, children=None, props={"href": "https://www.google.com", "target": "_blank"})
        node2 = HTMLNode(tag=None, value=None, children=None, props=None)
        self.assertNotEqual(node, node2)

    def test_html_to_props(self):
        node = HTMLNode(tag=None, value=None, children=None, props={"href": "https://www.google.com", "target": "_blank"})
        expcted_result = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(node.props_to_html(), expcted_result)

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_no_children(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.children, None)

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
        
    def test_to_html_many_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

    def test_headings(self):
        node = ParentNode(
            "h2",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>",
        )

if __name__ == "__main__":
    unittest.main()
