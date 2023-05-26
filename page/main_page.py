import allure
from selenium import webdriver
from selenium.webdriver.common.by import By

from page.search_page import SearchPage
from utils import wait_until


class MainPage:
    def __init__(self):
        # self.driver = webdriver.Chrome()
        self.driver = webdriver.Firefox()

    def to_search_advance(self) -> SearchPage:
        self.driver.get("https://ceshiren.com/")
        wait_until(self.driver, '#search-button[title=搜索]')
        allure.attach(body=self.driver.get_screenshot_as_png(), attachment_type=allure.attachment_type.PNG)

        self.driver.find_element(By.CSS_SELECTOR, '#search-button[title=搜索]').click()
        wait_until(self.driver, '.show-advanced-search')
        allure.attach(body=self.driver.get_screenshot_as_png(), attachment_type=allure.attachment_type.PNG)

        self.driver.find_element(By.CSS_SELECTOR, '.show-advanced-search').click()
        wait_until(self.driver, 'input.search-query')
        allure.attach(body=self.driver.get_screenshot_as_png(), attachment_type=allure.attachment_type.PNG)

        return SearchPage(self.driver)

    def close(self):
        self.driver.quit()

    def allure(self):
        ...
        # pytest --alluredir=allure  geektime_0/web/wework/reuse.py
        # allure serve allure/