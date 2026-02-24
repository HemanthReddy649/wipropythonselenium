from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://demowebshop.tricentis.com/login")
driver.maximize_window()

# Login
driver.find_element(By.ID, "Email").send_keys("your_email")
driver.find_element(By.ID, "Password").send_keys("your_password")
driver.find_element(By.CSS_SELECTOR, "input.login-button").click()

time.sleep(2)

# Go to Books section
driver.find_element(By.LINK_TEXT, "Books").click()

time.sleep(2)

# Add first book to cart
driver.find_element(By.CSS_SELECTOR, "input[value='Add to cart']").click()

time.sleep(2)

# Click shopping cart
driver.find_element(By.CLASS_NAME, "cart-label").click()

time.sleep(2)

# Validate item in cart
cart_text = driver.find_element(By.CLASS_NAME, "product-name").text
assert cart_text != ""

print("Product successfully added to cart!")

driver.quit()