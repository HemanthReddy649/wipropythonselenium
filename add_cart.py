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

# 3️⃣ Optional: Wait for page to load
time.sleep(2)

# 4️⃣ Find all products and their "Add to Cart" buttons
products = driver.find_elements(By.CSS_SELECTOR, "h4.product-name")
add_buttons = driver.find_elements(By.XPATH, "//div[@class='product-action']/button")

# 5️⃣ Loop through products and click "Add to Cart" for a specific item
target_product = "Tomato"
for i, product in enumerate(products):
    if target_product.lower() in product.text.lower():
        add_buttons[i].click()
        print(f"Added {product.text} to cart")
        break

# 6️⃣ Optional: Close browser after 3 seconds
time.sleep(3)
driver.quit()