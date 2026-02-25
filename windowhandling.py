import os.path
import time
from itertools import count

import pytest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

class Test_Windows:
    def test_window(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://the-internet.herokuapp.com/windows")
        driver.maximize_window()
        time.sleep(2)

        clickhere = driver.find_element(By.XPATH, "//a[normalize-space()='Click Here']")
        clickhere.click()

        windows = driver.window_handles
        print(windows)

        driver.switch_to.window(windows[1])

        text = driver.find_element(By.XPATH, "//h3[contains(text(),'New Window')]")
        print(text)
        driver.close()
        driver.switch_to.window(windows[0])
        clickhere.is_displayed()
        driver.close()