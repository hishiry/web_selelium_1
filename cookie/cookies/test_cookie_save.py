import json
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def test_cookie_get():
    driver = webdriver.Firefox()

    def loop_click(driver):
        # 显式等待 有的时候有些按钮是不生效
        # driver.find_element(By, value).click()(By.PARTIAL_LINK_TEXT, '添加成员')
        driver.get('https://work.weixin.qq.com/wework_admin/frame#index')
        sleep(60)
        return driver.find_element(By.CSS_SELECTOR, '.qrcode_wrap')
    WebDriverWait(driver, 600).until(loop_click)
    # WebDriverWait(driver, 600).until(expected_conditions.url_contains('wework_admin/frame'))
    cookies = driver.get_cookies()
    with open('cookies.json', 'w') as f:
        json.dump(cookies, f)


def test_cookie_user():
    with open('cookies.json') as f:
        cookies = json.load(f)

    driver = webdriver.Firefox()
    driver.get('https://work.weixin.qq.com/wework_admin/frame#index')

    for cookie in cookies:
        driver.add_cookie(cookie)
        print(cookie)
    driver.refresh()

