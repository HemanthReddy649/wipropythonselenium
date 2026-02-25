import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def setup():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))  # launch browser
    driver.maximize_window()  # maximize window
    driver.get("https://the-internet.herokuapp.com/tables")  # go to table page
    time.sleep(2)
    yield driver
    driver.quit()  # close browser


def test_table_data(setup):

    driver = setup

    # locate table rows and columns (TABLE 1)
    rows = driver.find_elements(By.CSS_SELECTOR, "#table1 tbody tr")  # all rows
    cols = driver.find_elements(By.CSS_SELECTOR, "#table1 thead th")  # all headers

    print("Number of Rows:", len(rows))  # print row count
    print("Number of Columns:", len(cols))  # print column count

    # print all rows
    for r_index, row in enumerate(rows, start=1):
        row_data = row.text.split(" ")  # split row text by space
        print(f"Row {r_index} data:", row_data)

    # fetch specific data: 3rd row, 3rd column (example)
    cell = driver.find_element(
        By.CSS_SELECTOR, "#table1 tbody tr:nth-child(3) td:nth-child(3)"
    ).text
    print("Specific cell [Row3,Col3]:", cell)

    time.sleep(3)