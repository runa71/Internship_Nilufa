from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep


class OffPlan(Page):
    Off_Plan = (By.CSS_SELECTOR,
                'address#w-node-_455f4786-676e-1311-ab71-82d622b51c3b-9b22b68b.menu-twobutton')  # div.menu-button-text
    Filter_Btn = (By.CSS_SELECTOR, '.filter-button')
    Out_Of_Stock = (By.CSS_SELECTOR, 'div[wized="priorityStatusOutOfStock"].tag-properties.margin-bottom-8')
    Out_Of_Stock_Tag = (By.CSS_SELECTOR, 'div[wized="projectStatus"]')

    def off_plan_menu(self, *locator):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.presence_of_element_located(self.Off_Plan))
        element.click()

    def right_page(self):
        return self.driver.current_url

    def click_filter(self, *locator):
        self.wait_for_element_clickable_click(*self.Filter_Btn)

    def filter_by_out_of_stock(self):
        self.click_filter()
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable(self.Out_Of_Stock))
        element.click()

    def verify_each_product_contains_sale_status_tag(self, expected_text, locator):
        # self.verify_text(expected_text, *locator)

        # actual_text = self.get_text(*locator)
        # assert expected_text == actual_text, f'Error, expected "{expected_text}" did not match actual "{actual_text}"'

        wait = WebDriverWait(self.driver, 20)
        element = wait.until(EC.visibility_of_element_located(locator))
        actual_text = element.text
        assert expected_text == actual_text, f'Error, expected "{expected_text}" did not match actual "{actual_text}"'