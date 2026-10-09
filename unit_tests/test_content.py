def test_menu_items():
    html = open("public/index.html").read()
    assert "Site Contents" in html
    assert "About Us" in html
    assert "Contact Us" in html
    assert 'action="https://formspree.io/f/dasaradhmandava@gmail.com"' in html
