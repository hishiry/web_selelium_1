import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from utils import wait_until


class SearchPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    """
    keyword : 搜索内容
    content_keyword : 
    posit : 点击位置 
    """
    def search(self, keyword, content_keyword, /, posit):
        if len(posit) > 0:
            for i in range(len(posit)-1):
                self.driver.find_element(By.CSS_SELECTOR, posit[i]).click()
                wait_until(self.driver, posit[i+1])
                allure.attach(body=self.driver.get_screenshot_as_png(), attachment_type=allure.attachment_type.PNG)

        query = self.driver.find_element(By.CSS_SELECTOR, 'input.search-query')
        # query.clear()
        if keyword != '':
            query.send_keys(keyword)

        content = self.driver.find_element(By.CSS_SELECTOR, posit[len(posit)-1])
        content.click()

        # 搜索发帖人需要输入内容
        if content_keyword != '':
            content.send_keys(content_keyword)
            wait_until(self.driver, '#search-posted-by-body .select-kit-collection li:first-child')
            allure.attach(body=self.driver.get_screenshot_as_png(), attachment_type=allure.attachment_type.PNG)
            self.driver.find_element(By.CSS_SELECTOR,
                                     '#search-posted-by-body .select-kit-collection li:first-child').click()

        self.driver.find_element(By.CSS_SELECTOR, '.search-bar .search-cta').click()
        # wait_until(self.driver, '.topic-title')
        return self

    def get_search_result(self, item_posit) -> list[str]:
        wait_until(self.driver, item_posit)
        allure.attach(body=self.driver.get_screenshot_as_png(), attachment_type=allure.attachment_type.PNG)
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

    def search_poster(self, keyword, poster) -> list[str]:
        posit = {0: '#search-type-header', 1: '.select-kit-collection li:first-child',
                 2: '.user-chooser', 3: '#search-posted-by-filter input:first-child'}

        self.search(keyword, poster, posit)

        wait_until(self.driver, '.author')
        allure.attach(body=self.driver.get_screenshot_as_png(), attachment_type=allure.attachment_type.PNG)
        result_list = []
        for element in self.driver.find_elements(By.XPATH, '//div[@class="search-results"]/div/div/div/div/a'):
            result_list.append(element.get_attribute('href'))
        print(result_list)
        print(str(result_list[0]))
        return result_list

    def search_matching_title_only(self, keyword) -> list[str]:
        posit = {0: '#matching-title-only'}
        return self.search(keyword, '', posit).get_search_result('.topic-title')

    def search_posted_date(self, keyword) -> list[str]:
        posit = {0: '#postTime-header', 1: '.select-kit-collection li:nth-child(2)',
                 2: '#search-post-date'}
        return self.search(keyword, '', posit).get_search_result('.topic-title')

    def login(self, username, password):
        self.driver.find_element(By.CSS_SELECTOR, '.login-button').click()
        self.driver.find_element(By.CSS_SELECTOR, '#login-account-name').send_keys(username)
        self.driver.find_element(By.CSS_SELECTOR, '#login-account-password').send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR, '#login-button').click()
        wait_until(self.driver, '#matching-title-only')
        allure.attach(body=self.driver.get_screenshot_as_png(), attachment_type=allure.attachment_type.PNG)

    def close(self):
        self.driver.quit()
