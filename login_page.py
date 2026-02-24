import time
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.firefox.service import service
from webdriver_manager.firefox import geckoDriverManger

driver = webdriver.firefox(service = service(geckoDriverManager().install()))
driver.maximize_window()
driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index')

time.sleep(4)
#enter username
name = driver.find_element(By_name, "username")
name.send_keys("Admin")

#enter password
password = driver.find_element(By.Name, "password")
password.send_keys("admin123")

time.sleep(4)
#click on login button

login = driver.find_element(By.XPATH, "//button[normalize-space()='Login']")
login.click()

assert "OrangeHRM" in driver.title