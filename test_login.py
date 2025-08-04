import pytest
import os
import time
import tempfile
import shutil
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def driver():
    # Create a temporary directory for unique Chrome profile
    user_data_dir = tempfile.mkdtemp()

    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument(f"--user-data-dir={user_data_dir}")  # Important for CircleCI

    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

    # Cleanup the temporary directory
    shutil.rmtree(user_data_dir, ignore_errors=True)

def test_login_success(driver):
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    assert "inventory" in driver.current_url, "Login failed or did not redirect to inventory page"

    timestamp = time.strftime("%Y%m%d_%H%M%S")
    driver.save_screenshot(f"reports/loginsuccess_{timestamp}.png") 

    print("Test passed: Login successfully")
    time.sleep(1)  # Shorter sleep for the  CircleCI
