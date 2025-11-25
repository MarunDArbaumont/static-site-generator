def markdown_to_blocks(markdown):
    splited_markdown = markdown.split("\n\n")
    good_blocks = []
    for block in splited_markdown:
        if block == "":
            continue
        block = block.strip()
        good_blocks.append(block)
    return good_blocks

