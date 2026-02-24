import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def setup():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()


def test_action_class_examples(setup):

    driver = setup
    actions = ActionChains(driver)

    # 1️ Right Click Example
    driver.get("https://demoqa.com/buttons")
    time.sleep(2)

    right_click_btn = driver.find_element(By.ID, "rightClickBtn")
    actions.context_click(right_click_btn).perform()
    print("Right Click Performed")
    time.sleep(2)

    # 2️ Double Click Example
    double_click_btn = driver.find_element(By.ID, "doubleClickBtn")
    actions.double_click(double_click_btn).perform()
    print("Double Click Performed")
    time.sleep(2)

    # 3️ Drag and Drop Example
    driver.get("https://demoqa.com/droppable")
    time.sleep(2)

    source = driver.find_element(By.ID, "draggable")
    target = driver.find_element(By.ID, "droppable")

    actions.drag_and_drop(source, target).perform()
    print("Drag and Drop Performed")
    time.sleep(2)

    # 4️ Click and Hold Example
    driver.get("https://demoqa.com/droppable")
    time.sleep(2)

    source = driver.find_element(By.ID, "draggable")
    actions.click_and_hold(source).move_by_offset(100, 0).release().perform()
    print("Click and Hold + Move Performed")
    time.sleep(2)

    # 5️ Keyboard Actions Example
    driver.get("https://demoqa.com/text-box")
    time.sleep(2)

    name_field = driver.find_element(By.ID, "userName")
    name_field.send_keys("Ramesh")
    time.sleep(1)

    # CTRL + A and CTRL + C
    actions.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()
    time.sleep(1)

    actions.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()
    print("Keyboard Copy Action Performed")
    time.sleep(2)