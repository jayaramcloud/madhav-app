import unittest

class TestContent(unittest.TestCase):
    def test_menu_items(self):
        html = open("public/index.html").read()
        self.assertIn("Site Contents", html)
        self.assertIn("Contact Us", html)

    def test_dropdown_structure(self):
        html = open("public/index.html").read()
        self.assertIn("sub", html)

    def test_address(self):
        html = open("public/index.html").read()
        self.assertIn("1223, Edmonton", html)
