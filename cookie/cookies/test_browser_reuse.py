from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def test_browser_reuse():
    option = Options()
    option.debugger_address = "127.0.0.1:9222"
    driver = webdriver.Chrome(options=option)
    driver.get("https://www.baidu.com")

    driver.current_window_handle
    driver.window_handles
    # driver.switch_to.window(window_handle)
    driver.switch_to.new_window('tab')
    driver.get("https://work.weixin.qq.com/wework_admin/frame")
    driver.switch_to.new_window('window')
    driver.get("https://work.weixin.qq.com/wework_admin/frame")
