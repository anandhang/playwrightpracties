from playwright.sync_api import  sync_playwright

"""
with sync_playwright() p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://example.com")
    print(page.title())
    browser.close()
"""

def addtwo():
    nums = [2,7,11,15]
    target = 9
    rnums = []
    for n in nums:
        i = 0
        firstItem = n
        for m in nums:
            j = 0
            secItem = m
            if firstItem + secItem == target and i != j:
                rnums[0] = firstItem
                rnums[1] = secItem
                return rnums
    
result = addtwo()
print(result)