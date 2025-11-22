from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

browser = webdriver.Chrome()
browser.get('http://www.taobao.com')

try:
    element = WebDriverWait(browser, 5, poll_frequency=0.5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '.nav-bd a'))
    )
    print(element.text)
    print('元素已加载完毕')
    element.click()
    handles = browser.window_handles
    print('所有窗口句柄:', handles)
    print('当前窗口句柄:', browser.current_window_handle)
    time.sleep(5)
    browser.switch_to.window(handles[0])
    browser.switch_to.window(handles[-1])
    time.sleep(2)
    browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    time.sleep(20)
except Exception as e:
    print(repr(e))
