import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_1(self):
        node = TextNode("This is the first text node.", TextType.ITALIC)
        node2 = TextNode("Haha Birdman.", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_2(self):
        node = TextNode("This is the second test", TextType.BOLD)
        node2 = TextNode("This is the second test", TextType.BOLD, "boot.dev")
        self.assertNotEqual(node, node2)

    def test_3(self):
        node = TextNode("This is the third test.", TextType.ITALIC)
        node2 = TextNode("This is the third test.", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_equal_all_fields(self):
        a = TextNode("Same", TextType.LINK, "https://boot.dev")
        b = TextNode("Same", TextType.LINK, "https://boot.dev")
        self.assertEqual(a, b)

if __name__ == "__main__":
    unittest.main()