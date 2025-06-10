from selenium import webdriver
from selenium.webdriver.common.by import By
import time

options = Options()
options.add_argument("--headless")  # Run headless
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1920,1080")  # Make sure page is fully visible
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)
driver.get("https://www.saucedemo.com/")
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

assert "inventory" in driver.current_url


print("Test passed: Login successful!")
driver.save_screenshot("login_success.png")
time.sleep(3)
driver.quit()
