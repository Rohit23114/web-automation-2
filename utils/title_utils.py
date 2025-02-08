def check_title(driver):
    """
    Verifies if the page title contains 'Swag Labs'.
    """
    title = driver.title
    return "Swag Labs" in title
