import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def setup():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))  # launch Chrome
    driver.maximize_window()  # maximize window
    driver.get("https://jqueryui.com/datepicker/")  # navigate to jQuery UI Datepicker page
    time.sleep(2)
    yield driver
    driver.quit()  # close browser


def test_datepicker_in_frame(setup):

    driver = setup

    driver.switch_to.frame(driver.find_element(By.CSS_SELECTOR, ".demo-frame"))  # switch to iframe
    time.sleep(1)

    date_input = driver.find_element(By.ID, "datepicker")  # locate date input
    date_input.click()  # open calendar
    time.sleep(1)

    driver.find_element(By.XPATH, "//a[text()='15']").click()  # select date 15
    time.sleep(2)

    selected_date = date_input.get_attribute("value")  # get selected value
    print("Selected date:", selected_date)

    assert "15" in selected_date  # verify date contains 15