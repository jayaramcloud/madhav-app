from playwright.sync_api import Page

def test_menu(page: Page):
    page.goto("https://madhav.preparingforinterviews.com")
    assert "Dasaradh" in page.content()
