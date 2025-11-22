from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time


try:
    
    time1 = time.time()

    options = Options()
    options.add_argument('--headless=new')
    service = Service(executable_path='./chromedriver.exe')
    driver = webdriver.Chrome(options=options, service=service)


    time2 = time.time()

    print('启动浏览器耗时:', time2 - time1, '秒')
    driver.get('https://weather.cma.cn/web/weather/54846.html')

    time3 = time.time() 

    print('加载页面耗时:', time3 - time2, '秒')
    time4 = time.time()

    temperature_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, '#temperature')
        )
    )

    time5 = time.time()

    print('定位温度元素耗时:', time5 - time4, '秒')
    temperature = temperature_element.text
    print('当前温度:', temperature)
except TimeoutException:
    print('等待超时：未能在指定时间内定位到温度元素')
except Exception as e:
    print('发生错误:', repr(e))
finally:
    driver.close()
    print('总运行时间:', time5 - time1, '秒')