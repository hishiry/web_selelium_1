from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from utils import wait_until


class SearchPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def search(self, search_keyword, keyword, /, posit):
        for i in range(len(posit)-1):
            self.driver.find_element(By.CSS_SELECTOR, posit[i]).click()
            wait_until(self.driver, posit[i+1])

        self.driver.find_element(By.CSS_SELECTOR, posit[len(posit)-1]).click()
        try:
            if keyword != '':
                posit[-1].send_keys(keyword)
        except (RuntimeError, TypeError, NameError, KeyError):
            pass

        query = self.driver.find_element(By.CSS_SELECTOR, 'input.search-query')
        query.clear()
        query.send_keys(search_keyword)
        self.driver.find_element(By.CSS_SELECTOR, '.search-bar .search-cta').click()
        # wait_until(self.driver, '.topic-title')
        return self

    def get_search_result(self, item_posit) -> list[str]:
        wait_until(self.driver, item_posit)
        title_list = []
        for element in self.driver.find_elements(By.CSS_SELECTOR, item_posit):
            title_list.append(element.text)
        print(title_list)
        print(str(title_list[0]))
        return title_list

    def search_topic(self, keyword) -> list[str]:
        posit = {0: '#search-type-header', 1: '.select-kit-collection li:first-child'}
        return self.search(keyword, '', posit).get_search_result('.topic-title')

    def search_category(self, keyword) -> list[str]:
        posit = {0: '#search-type-header', 1: '.select-kit-collection li:nth-child(2)'}
        return self.search(keyword, '', posit).get_search_result('.fps-tag-item')

    def search_user(self, keyword) -> list[str]:
        posit = {0: '#search-type-header', 1: '.select-kit-collection li:last-child'}
        return self.search(keyword, '', posit).get_search_result('.username')

    def search_poster(self, keyword) -> list[str]:
        posit = {0: '#search-type-header', 1: '.select-kit-collection li:first-child',
                 2: '.user-chooser', 3: '#search-posted-by-filter'}
        return self.search(keyword, 'seven', posit).get_search_result('.topic-title')

    def close(self):
        self.driver.quit()
