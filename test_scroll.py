import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def setup():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("https://rahulshettyacademy.com/AutomationPractice/")
    time.sleep(3)
    yield driver
    driver.quit()


def test_all_scroll_examples(setup):
    driver = setup

    # 1️ Scroll Down Full Page
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    print("Scrolled to bottom")
    time.sleep(2)

    # 2️ Scroll Up Full Page
    driver.execute_script("window.scrollTo(0, 0);")
    print("Scrolled to top")
    time.sleep(2)

    # 3️ Scroll By Pixel (Down 500px)
    driver.execute_script("window.scrollBy(0, 500);")
    print("Scrolled down 500 pixels")
    time.sleep(2)

    # 4️ Scroll By Pixel (Up 300px)
    driver.execute_script("window.scrollBy(0, -300);")
    print("Scrolled up 300 pixels")
    time.sleep(2)

    # 5️ Scroll Until Element Visible
    element = driver.find_element(By.ID, "mousehover")
    driver.execute_script("arguments[0].scrollIntoView(true);", element)
    print("Scrolled until specific element visible")
    time.sleep(2)

    # 6️ Smooth Scroll Down Slowly
    for i in range(0, 1000, 100):
        driver.execute_script(f"window.scrollTo(0, {i});")
        time.sleep(1)
    print("Smooth scrolling done")
    time.sleep(2)

    # 7️ Scroll Inside a Web Table
    table = driver.find_element(By.XPATH, "//div[@class='tableFixHead']")
    driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", table)
    print("Scrolled inside table")
    time.sleep(2)

    # 8️ Horizontal Scroll (if available)
    driver.execute_script("window.scrollBy(500, 0);")
    print("Horizontal scroll")
    time.sleep(2)