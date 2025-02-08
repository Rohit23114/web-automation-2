from selenium.webdriver.common.by import By
from time import sleep

def login(driver, username, password):
    """
    Performs login on the specified website using the provided credentials.
    """
    driver.get("https://www.saucedemo.com/")
    sleep(3)
    
    driver.find_element(By.ID, "user-name").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()
    sleep(5)

def check_login_success(driver):
    """
    Verifies if the login was successful by checking for the 'products' text on the page.
    """
    text = driver.find_element(By.CLASS_NAME, "title").text
    return "products" in text.lower()
