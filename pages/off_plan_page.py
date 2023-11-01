from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

class OffPlan(Page):

     Off_Plan = (By.CSS_SELECTOR, 'address#w-node-_455f4786-676e-1311-ab71-82d622b51c3b-9b22b68b.menu-twobutton')  # div.menu-button-text
     Off_Plan_Mobile = (By.CSS_SELECTOR, '[wized="mobileMenuForVerifiedUsers"] > [aria-current="page"]')
     Off_Plan_Page = (By.CSS_SELECTOR,'div.page-title')
     Filter_Btn_Web = (By.CSS_SELECTOR, '.filter-button')
     Filter_Btn_Mobile = (By.CSS_SELECTOR, 'div.filter-button')
     Out_Of_Stock = (By.CSS_SELECTOR, 'div[wized="priorityStatusOutOfStock"].tag-properties.margin-bottom-8')
     Out_Of_Stock_Tag = (By.CSS_SELECTOR, 'div[wized="projectStatus"]')

     def off_plan_menu_web(self, *locator):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.presence_of_element_located(self.Off_Plan))
        element.click()

     #def off_plan_menu_mobile(self, *locator):
        #wait = WebDriverWait(self.driver, 10)
        #element = wait.until(EC.presence_of_element_located(self.Off_Plan_Mobile))
        #element.click()

     def right_page(self):
        return self.driver.current_url

     def click_filter(self, *locator):
        self.wait_for_element_clickable_click(*self.Filter_Btn_Web)
        #self.wait_for_element_clickable_click(*self.Filter_Btn_Mobile)

     def filter_by_out_of_stock(self):
        self.click_filter()
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable(self.Out_Of_Stock))
        element.click()
        self.wait_for_element_clickable_click(*self.Out_Of_Stock)

        ## Wait for the filter to load and scroll to the element if needed
        #self.click_filter()
        #wait = WebDriverWait(self.driver, 10)
        #element = wait.until(EC.presence_of_element_located(self.Out_Of_Stock))
        #actions = ActionChains(self.driver)
        #actions.move_to_element(element).perform()

        ## Wait for the element to be clickable and click it
        #wait.until(EC.element_to_be_clickable(self.Out_Of_Stock)).click()


     def verify_each_product_contains_sale_status_tag(self, expected_text, locator):
        # self.verify_text(expected_text, *locator)

        # actual_text = self.get_text(*locator)
        # assert expected_text == actual_text, f'Error, expected "{expected_text}" did not match actual "{actual_text}"'

        wait = WebDriverWait(self.driver, 20)
        element = wait.until(EC.visibility_of_element_located(locator))
        actual_text = element.text
        assert expected_text == actual_text, f'Error, expected "{expected_text}" did not match actual "{actual_text}"'
