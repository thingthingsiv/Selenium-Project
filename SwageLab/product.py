from selenium.webdriver.common.by import By

def choose_products(driver, product_names):

    products = driver.find_elements(By.CLASS_NAME, "inventory_item")
    for product_name in product_names:
        for product in products:
            name = product.find_element(By.CLASS_NAME, "inventory_item_name").text
            if name == product_name:
                product.find_element(By.CLASS_NAME, "btn_inventory").click()
                break
