from selenium.webdriver.common.by import By

def checkout(driver, first_name, last_name, postal_code):
    driver.find_element(By.ID, "checkout").click()
    driver.find_element(By.ID, "first-name").send_keys(first_name)
    driver.find_element(By.ID, "last-name").send_keys(last_name)
    driver.find_element(By.ID, "postal-code").send_keys(postal_code)
    driver.find_element(By.ID, "continue").click()
    driver.find_element(By.ID, "finish").click()
