from enum import Enum
from htmlnode import LeafNode

class TextType (Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = TextType(text_type)  
        self.url = url

    def __eq__(self, value):
        if (self.text == value.text and self.text_type == value.text_type and self.url == value.url):
            return True
        
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"

def text_node_to_html_node(value):
    match value.text_type:
        case TextType.TEXT:
            return LeafNode(None, value.text)
        case TextType.BOLD:
            return LeafNode("b", value.text)
        case TextType.ITALIC:
            return LeafNode("i", value.text)
        case TextType.CODE:
            return LeafNode("code", value.text)
        case TextType.LINK:
            return LeafNode("a", value.text, {"href" : value.url})
        case TextType.IMAGE:
            return LeafNode("img", None, {"src" : value.url, "alt": value.text})
        case _:
            raise Exception("This is not a text type")

