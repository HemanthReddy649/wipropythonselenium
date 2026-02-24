from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# 1️⃣ Setup Chrome
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

# 2️⃣ Open the site
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
time.sleep(2)  # wait for page to load

# 3️⃣ Find all products
products = driver.find_elements(By.CSS_SELECTOR, "div.product")

# 4️⃣ Loop through each product and print details
for product in products:
    name = product.find_element(By.CSS_SELECTOR, "h4.product-name").text
    price = product.find_element(By.CSS_SELECTOR, "p.product-price").text
    button = product.find_element(By.CSS_SELECTOR, "div.product-action > button")

    print(f"Product Name: {name}, Price: {price}")

    # Optional: Click Add to Cart for a specific item
    if "Tomato" in name:
        button.click()
        print(f"Added {name} to cart")

time.sleep(3)
driver.quit()