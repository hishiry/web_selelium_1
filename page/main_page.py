import os
from time import sleep
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from page.search_page import SearchPage
from utils import wait_until


class MainPage:
    def __init__(self):
        # self.driver = webdriver.Chrome()
        # self.driver = webdriver.Firefox()

        browser = os.getenv('browser')
        if browser == 'chrome':
            options = webdriver.ChromeOptions()
        elif browser == 'firefox':
            options = webdriver.FirefoxOptions()
        else:
            options = webdriver.ChromeOptions()

        self.driver = webdriver.Remote('http://192.168.111.137:14444/wd/hub', options=options)
        self.driver.implicitly_wait(5)

    def to_search_advance(self) -> SearchPage:
        # 打开浏览器
        self.driver.get("https://ceshiren.com/")
        ## remote 不识别中文
        # wait_until(self.driver, '#search-button[title=搜索]')
        wait_until(self.driver, '.search-dropdown')
        allure.attach(body=self.driver.get_screenshot_as_png(), attachment_type=allure.attachment_type.PNG)

        self.driver.find_element(By.CSS_SELECTOR, '.search-dropdown').click()
        wait_until(self.driver, '.show-advanced-search')
        allure.attach(body=self.driver.get_screenshot_as_png(), attachment_type=allure.attachment_type.PNG)

        self.driver.find_element(By.CSS_SELECTOR, '.show-advanced-search').click()
        wait_until(self.driver, 'input.search-query')
        allure.attach(body=self.driver.get_screenshot_as_png(), attachment_type=allure.attachment_type.PNG)

        # def loop_click(driver):
        #     # 显式等待 有的时候有些按钮是不生效
        #     # driver.find_element(By, value).click()(By.PARTIAL_LINK_TEXT, '添加成员')
        #     driver.get('https://ceshiren.com/search?expanded=true')
        #     sleep(20)
        #     return driver.find_element(By.CSS_SELECTOR, 'input.search-query')
        # WebDriverWait(self.driver, 600).until(loop_click)

        return SearchPage(self.driver)

    def close(self):
        self.driver.quit()

    def allure(self):
        ...
        # pytest --alluredir=allure  geektime_0/web/wework/reuse.py
        # allure serve allure/