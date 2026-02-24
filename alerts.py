from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://trytestingthis.netlify.app/")

# -------- Dropdown 1 --------
dropdown1 = Select(driver.find_element(By.ID, "option"))
dropdown1.select_by_visible_text("Option 1")
time.sleep(2)

# -------- Dropdown 2 --------
dropdown2 = Select(driver.find_element(By.ID, "owc"))

dropdown2.select_by_visible_text("Option")
time.sleep(2)

dropdown2.select_by_visible_text("Option 2")   # ✅ safest
# OR dropdown2.select_by_value("option2")

time.sleep(2)

dropdown2.select_by_index(3)
time.sleep(2)

driver.quit()