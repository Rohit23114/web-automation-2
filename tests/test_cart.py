import pytest
from utils.driver import create_driver
from utils.cart_utils import add_to_cart, remove_from_cart, get_cart_value

def test_add_to_cart():
    driver = create_driver()
    try:
        add_to_cart(driver, num_items=3)
        cart_value = get_cart_value(driver)
        assert "3" in cart_value, "Add to cart test failed"
        print("TEST PASSED: Items added to the cart.")
    finally:
        driver.quit()

def test_remove_from_cart():
    driver = create_driver()
    try:
        add_to_cart(driver, num_items=3)
        remove_from_cart(driver, num_items=2)
        cart_value = get_cart_value(driver)
        assert "1" in cart_value, "Remove from cart test failed"
        print("TEST PASSED: Items removed from the cart.")
    finally:
        driver.quit()
