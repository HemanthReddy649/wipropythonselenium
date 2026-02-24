from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

#  Setup Chrome
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

#  Open SauceDemo
driver.get("https://www.saucedemo.com/")
time.sleep(2)

#  Login
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()
time.sleep(2)

#  Inspect all products
products = driver.find_elements(By.CLASS_NAME, "inventory_item")
for product in products:
    name = product.find_element(By.CLASS_NAME, "inventory_item_name").text
    price = product.find_element(By.CLASS_NAME, "inventory_item_price").text
    print(f"Product: {name}, Price: {price}")

#  Optional: Click Add to Cart for first item
first_add_button = products[0].find_element(By.TAG_NAME, "button")
first_add_button.click()
print("Added first item to cart")

time.sleep(3)
driver.quit()