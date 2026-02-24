import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


class Test_Actions:

    def test_action(self):

        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.get("https://www.amazon.in/")
        time.sleep(4)
        actions = ActionChains(driver)
        bestsellers = driver.find_element(By.XPATH, "//a[normalize-space()='Bestsellers']")
        actions.double_click(bestsellers).perform()
        time.sleep(4)
        driver.back()
        time.sleep(2)
        mobiles = driver.find_element(By.XPATH, "//a[normalize-space()='Bestsellers']")
        actions.context_click().perform()
        time.sleep(2)
        driver.close()