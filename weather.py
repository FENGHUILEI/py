from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time


try:
    
    begin_time = time.time()
    print('程序开始运行...')

    options = Options()
    options.add_argument('--headless=new')
    service = Service(executable_path='./chromedriver.exe')
    driver = webdriver.Chrome(options=options, service=service)

    driver.get('https://weather.cma.cn/web/weather/54846.html')
    wait = WebDriverWait(driver, 10)

    info_dict = dict()

    info = wait.until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, '[class="pull-left day actived"]')     
        )
    ).text.split('\n')

    info_dict['天气'] = info[2]
    info_dict['风向'] = info[3]
    info_dict['风力'] = info[4]
    info_dict['最高温'] = info[5]
    info_dict['最低温'] = info[6]

    for key, value in info_dict.items():
        print(f'{key}: {value}')

except TimeoutException:
    print('等待超时：未能在指定时间内定位到温度元素')
except Exception as e:
    print('发生错误:', repr(e))
finally:
    driver.close()
    end_time = time.time()
    print('总运行时间:', end_time - begin_time, '秒')