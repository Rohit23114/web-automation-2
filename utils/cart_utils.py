from selenium.webdriver.common.by import By
from time import sleep

def add_to_cart(driver, num_items=3):
    """
    Adds the specified number of items to the cart on the page.
    """
    driver.get("https://www.saucedemo.com/")
    sleep(3)
    
    add_to_cart_btns = driver.find_elements(By.CLASS_NAME, "btn_inventory")
    for btn in add_to_cart_btns[:num_items]:
        btn.click()

def remove_from_cart(driver, num_items=2):
    """
    Removes the specified number of items from the cart on the page.
    """
    driver.get("https://www.saucedemo.com/")
    sleep(3)

    add_to_cart_btns = driver.find_elements(By.CLASS_NAME, "btn_inventory")
    for btn in add_to_cart_btns[:num_items]:
        btn.click()

    remove_btns = driver.find_elements(By.CLASS_NAME, "btn_inventory")
    for btn in remove_btns[:num_items]:
        btn.click()

def get_cart_value(driver):
    """
    Returns the current number of items in the shopping cart.
    """
    cart_value = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
    return cart_value.text
