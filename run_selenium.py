print("Script Started")

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_argument("--start-maximized")

service = Service(ChromeDriverManager().install())

driver = webdriver.Chrome(service=service, options=options)

driver.get("https://www.google.com")

input("Press Enter to close browser...")
driver.quit()