from playwright.sync_api import Page

class HomePage:

    def __init__(self, page:Page):
        self.page = page
        self.Upgrade_button = page.get_by_role("button", name="Upgrade")
        self.Performance_link = page.get_by_role("link", name="Performance")
        self.Dashboard_link = page.get_by_role("link", name="Dashboard")


    def is_upgrade_button_Visible(self):
        return self.Upgrade_button.is_visible()

    def click_perfomance_link(self):
        self.Performance_link.click()

    def click_Dashboard_link(self):
        self.Dashboard_link.click()
        