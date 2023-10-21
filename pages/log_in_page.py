from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep
class LoginPage(Page):

    SIGN_IN_LINK = (By.CSS_SELECTOR, '.sing-in-text')
    SIGNIN_INPUT_EMAIL = (By.ID, "email-2")
    PASSWORD_INPUT = (By.ID, "field")
    CONTINUE_BUTTON = (By.CSS_SELECTOR, 'a.login-button')

    def login_pages(self):
        self.open_url('sign-up')

    def click_on_signin_link(self):
        self.click(*self.SIGN_IN_LINK)


    def input_email(self,text):
        self.input_text(text, *self.SIGNIN_INPUT_EMAIL)


    def input_password(self,text):
        self.input_text(text, *self.PASSWORD_INPUT)


    def click_continue(self):
        self.click(*self.CONTINUE_BUTTON)


    def right_page(self):
        self.verify_partial_url('')