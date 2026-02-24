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
    driver.get("https://the-internet.herokuapp.com/upload")
    time.sleep(2)
    yield driver
    driver.quit()


def test_file_upload(setup):
    driver = setup

    # 1️ Locate File Input
    file_input = driver.find_element(By.ID, "file-upload")

    # Provide the path to the file you want to upload
    # Replace this with any file path on your machine
    file_path = r""

    # Upload file using send_keys
    file_input.send_keys(file_path)
    print("File selected for upload")
    time.sleep(2)

    # 2️ Click Upload Button
    driver.find_element(By.ID, "file-submit").click()
    print("Upload button clicked")
    time.sleep(3)

    # 3️ Validate Success
    success_text = driver.find_element(By.TAG_NAME, "h3").text
    print("Upload status:", success_text)

    assert "File Uploaded!" in success_text
    print("File uploaded successfully")