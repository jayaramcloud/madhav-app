import unittest

class TestContent(unittest.TestCase):
    def test_menu_items(self):
        html = open("public/index.html").read()
        self.assertIn("Site Contents", html)
        self.assertIn("Contact Us", html)
