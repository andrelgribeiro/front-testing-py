from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

class FrontPageObjects:
    def __init__(self, driver):
        self.driver = driver

    def check_first_checkbox(self):
        checkbox = self.driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")[0]
        if not checkbox.is_selected():
            checkbox.click()

    def uncheck_first_checkbox(self):
        checkbox = self.driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")[0]
        if checkbox.is_selected():
            checkbox.click()

    def is_first_checkbox_checked(self):
        checkbox = self.driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")[0]
        return checkbox.is_selected()

    def drag_and_drop(self):
        element_a = self.driver.find_element(By.ID, 'column-a')
        element_b = self.driver.find_element(By.ID, 'column-b')
        action = ActionChains(self.driver)
        action.drag_and_drop(element_a, element_b).perform()

    def is_drag_successful(self):
        element_a = self.driver.find_element(By.ID, 'column-a')
        return "B" in element_a.text
