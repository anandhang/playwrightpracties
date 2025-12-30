import re
from playwright.sync_api import Playwright, sync_playwright, expect, Page
import pytest

@pytest.mark.parametrize(
    "username,password",
    [("Admin", "admin123"),
     ("user1","password01")
    ],
)
def test_dddemo(page: Page, username, password) -> None:
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    page.get_by_role("textbox", name="Username").click()
    page.get_by_role("textbox", name="Username").fill(username)
    page.get_by_role("textbox", name="Password").click()
    page.get_by_role("textbox", name="Password").fill(password)
    page.get_by_role("button", name="Login").click()
    expect(page.get_by_role("button", name="Upgrade")).to_be_visible()
