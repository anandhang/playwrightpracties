import re
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.home_page import HomePage


def test_example(page: Page) -> None:
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    loginPage = LoginPage(page)
    homePage = HomePage(page)

    loginPage.click_username()
    loginPage.enter_username("Admin")
    loginPage.click_password()
    loginPage.enter_password("admin123")
    loginPage.click_login()
    homePage.is_upgrade_button_Visible()
    homePage.click_perfomance_link()
    expect(page.get_by_role("button", name="Search")).to_be_visible()

    page.get_by_role("button", name="Search").click()
    expect(page.locator("#app")).to_contain_text("No Records Found")
    page.get_by_role("link", name="Dashboard").click()
    expect(page.locator("#app")).to_contain_text("Time at Work")
    expect(page.locator("#app")).to_contain_text("My Actions")
    expect(page.locator("#app")).to_contain_text("Quick Launch")
    expect(page.locator("#app")).to_contain_text("Buzz Latest Posts")
    page.get_by_role("listitem").filter(has_text="shanka pratapsingh").locator("i").click()
    page.get_by_role("menuitem", name="Logout").click()
    loginPage.enter_username("")
    loginPage.enter_password("")
