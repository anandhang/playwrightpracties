import re
from playwright.sync_api import expect

def test_google_search(page):
    page.wait_for_timeout(3000)
    page.goto("https://www.google.com/")
    
    try:
        page.get_by_role("button", name="Not interested").click(timeout=5000)
    except:
        print("No popup to axcept")

    page.get_by_role("combobox", name="Search").fill("Playwright")

    page.keyboard.press("Enter")

    #expect(page.locator("h1")).to_have_text(re.compile("Playwright", re.IGNORECASE))

    expect(page).to_have_text(re.compile("Playwright"), re.IGNORECASE)