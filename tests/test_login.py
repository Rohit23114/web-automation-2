import pytest
from utils.driver import create_driver
from utils.login_utils import login, check_login_success

def test_login():
    driver = create_driver()
    try:
        login(driver, "standard_user", "secret_sauce")
        assert check_login_success(driver), "Login test failed"
        print("TEST PASSED: Login successful.")
    finally:
        driver.quit()
