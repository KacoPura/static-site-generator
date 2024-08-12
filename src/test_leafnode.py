import unittest
from htmlnode import LeafNode

class TestLeafNode(unittest.TestCase):

	def test_to_html_with_tag_and_props(self):
    		node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
    		result = node.to_html()
    		self.assertEqual(result, '<a href="https://www.google.com">Click me!</a>')

	def test_to_html_with_tag_no_props(self):
		node = LeafNode("p", "This is a paragraph of text.")
		result = node.to_html()
		self.assertEqual(result, '<p>This is a paragraph of text.</p>')

	def test_to_html_no_tag(self):
		node = LeafNode(None, "Just some text")
		result = node.to_html()
		self.assertEqual(result, 'Just some text')

	def test_to_html_no_value(self):
		with self.assertRaises(ValueError):
			LeafNode("p", "").to_html()

if __name__ == "__name__":
	unittest.main
