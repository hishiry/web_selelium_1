from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def wait_until(driver, posit):
    WebDriverWait(driver, 20).until(
        expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, posit)))


# class Utils:
#     def __init__(self):
#         ...
#
#     def wait_until(self, driver, posit):
#         WebDriverWait(driver, 20).until(
#             expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, posit)))
#         return self
