import pytest
from utils.driver import create_driver
from utils.title_utils import check_title

def test_title():
    driver = create_driver()
    try:
        driver.get("https://www.saucedemo.com/")
        assert check_title(driver), "Title test failed"
        print("TEST PASSED: Title is correct.")
    finally:
        driver.quit()
