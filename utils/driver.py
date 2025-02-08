from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def create_driver():
    """
    Initializes and returns a Chrome WebDriver with specified options.
    """
    options = Options()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(options=options)
    return driver
