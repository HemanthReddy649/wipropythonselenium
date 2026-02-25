import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def setup():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("https://rsuitejs.com/components/date-picker/")
    yield driver
    driver.quit()


def test_select_date(setup):

    driver = setup
    wait = WebDriverWait(driver, 15)

    # Scroll to first date picker
    date_input = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "input[aria-haspopup='dialog']"))
    )

    driver.execute_script("arguments[0].scrollIntoView(true);", date_input)
    time.sleep(2)

    # Click date picker input
    date_input.click()
    print("Calendar opened")
    time.sleep(2)

    # Select a specific day (example: 25)
    day = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//div[contains(@class,'rs-calendar')]//span[text()='25']"))
    )

    day.click()
    print("Date selected successfully ")

    time.sleep(3)