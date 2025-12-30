import re
from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    page.get_by_role("textbox", name="Username").click()
    page.get_by_role("textbox", name="Username").fill("Admin")
    page.get_by_role("textbox", name="Password").click()
    page.get_by_role("textbox", name="Password").fill("admin123")
    page.get_by_role("button", name="Login").click()
    expect(page.get_by_role("button", name="Upgrade")).to_be_visible()
    page.get_by_role("link", name="Performance").click()
    expect(page.get_by_role("button", name="Search")).to_be_visible()
    page.get_by_role("button", name="Search").click()
    expect(page.locator("#app")).to_contain_text("No Records Found")
    page.get_by_role("link", name="Dashboard").click()
    expect(page.locator("#app")).to_contain_text("Time at Work")
    page.get_by_text("My Actions").click()
    expect(page.locator("#app")).to_contain_text("My Actions")
    expect(page.locator("#app")).to_contain_text("Quick Launch")
    expect(page.locator("#app")).to_contain_text("Buzz Latest Posts")
    page.get_by_role("listitem").filter(has_text="manda user").locator("i").click()
    page.get_by_role("menuitem", name="Logout").click()
