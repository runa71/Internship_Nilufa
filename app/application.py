from pages.main_page import MainPage
from pages.off_plan_page import OffPlan
from pages.log_in_page import LoginPage


class Application:
 #updated
    def __init__(self, driver):
        self.main_page = MainPage(driver)
        self.off_plan_page = OffPlan(driver)
        self.log_in_page = LoginPage(driver)