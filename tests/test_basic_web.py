from playwright.sync_api import Page, expect

def test_google_title(page: Page):
    page.goto("https://www.google.com")
    expect(page).to_have_title("Google")

def test_saucedemo_login_page(page: Page):
    page.goto("https://www.saucedemo.com")
    expect(page.locator(".login_logo")).to_be_visible()