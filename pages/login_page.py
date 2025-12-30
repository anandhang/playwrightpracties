from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page:Page):
        self.page = page
        self.username_input = page.get_by_role("textbox", name="Username")
        self.password_input = page.get_by_role("textbox", name="Password")
        self.login_button = page.get_by_role("button", name="Login")
        
    def enter_username(self, username: str):
        self.username_input.fill(username)
    
    def enter_password(self, password: str):
        self.password_input.fill(password)

    def click_login(self):
        self.login_button.click()

    def click_username(self):
        self.username_input.click()

    def click_password(self):
        self.password_input.click()

    def login(self, username: str, password: str):
        self.click_username()
        self.enter_username(username)
        self.click_password()
        self.enter_password(password)
        self.click_login()
