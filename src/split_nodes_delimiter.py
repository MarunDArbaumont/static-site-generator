from textnode import TextType, TextNode
from extract import extract_markdown_links, extract_markdown_images

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        new_node = []
        splited_text = node.text.split(delimiter)
        if len(splited_text) % 2 == 0:
            raise ValueError("invalid markdown, formatted section not closed")
        for i in range(len(splited_text)):
            if splited_text[i] == "":
                continue
            if i % 2 == 0:
                new_node.append(TextNode(splited_text[i], TextType.TEXT))
            else:
                new_node.append(TextNode(splited_text[i], text_type))
        new_nodes.extend(new_node)
    return new_nodes

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        extracted_images = extract_markdown_images(node.text)
        if len(extracted_images) == 0:
            new_nodes.append(node)
            continue
        new_node = []
        updated_text = node.text
        for image in extracted_images:
            splited_text = updated_text.split(f"![{image[0]}]({image[1]})", 1)
            if splited_text[0] != "":
                new_node.append(TextNode(splited_text[0], TextType.TEXT))
            new_node.append(TextNode(image[0], TextType.IMAGE, image[1]))
            updated_text = splited_text[1]
        if updated_text != "":
            new_node.append(TextNode(updated_text, TextType.TEXT))
        new_nodes.extend(new_node)
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        extracted_links = extract_markdown_links(node.text)
        if len(extracted_links) == 0:
            new_nodes.append(node)
            continue
        new_node = []
        updated_text = node.text
        for link in extracted_links:
            splited_text = updated_text.split(f"[{link[0]}]({link[1]})", 1)
            if splited_text[0] != "":
                new_node.append(TextNode(splited_text[0], TextType.TEXT))
            new_node.append(TextNode(link[0], TextType.LINK, link[1]))
            updated_text = splited_text[1]
        if updated_text != "":
            new_node.append(TextNode(updated_text, TextType.TEXT))
        new_nodes.extend(new_node)
    return new_nodes
        