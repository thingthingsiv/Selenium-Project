from selenium.webdriver.common.by import By

def view_cart(driver):
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
