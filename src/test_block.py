import unittest
from block import BlockType, block_to_block_type

class TestBlock(unittest.TestCase):
    def test_block_paragraph(self):
        block = block_to_block_type(
            "Simple paragraph"
        )
        self.assertEqual(BlockType.PARAGRAPH, block)

    def test_block_heading(self):
        block = block_to_block_type(
            "# This is a heading"
        )
        self.assertEqual(BlockType.HEADING, block)

    def test_block_code(self):
        block = block_to_block_type(
            "```\ncode\n```"
        )
        self.assertEqual(BlockType.CODE, block)

    def test_block_undordered_list(self):
        block = block_to_block_type(
            "- This is a list"
        )
        self.assertEqual(BlockType.UNORDERED_LIST, block)

    def test_block_orderd_list(self):
        block = block_to_block_type(
            "1. This is an ordered list"
        )
        self.assertEqual(BlockType.ORDERED_LIST, block)

if __name__ == "__main__":
    unittest.main()
    