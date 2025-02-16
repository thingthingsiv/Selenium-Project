from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
import time

# Initialize WebDriver
service = Service("/Users/lychandy/Documents/chromedriver")
driver = webdriver.Chrome(service=service)

try:
    # Open the URL
    driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
    driver.maximize_window()

    # Wait for the page to load
    time.sleep(2)

    # Search for an item
    search_box = driver.find_element(By.CSS_SELECTOR, "input.search-keyword")
    search_box.send_keys("banana")
    time.sleep(2)

    # Add the item to the cart
    add_to_cart_button = driver.find_element(By.XPATH, "//button[text()='ADD TO CART']")
    add_to_cart_button.click()
    time.sleep(2)

    # Go to the cart
    cart_icon = driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']")
    cart_icon.click()

    proceed_to_checkout = driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']")
    proceed_to_checkout.click()

    # Verify the item is in the cart
    time.sleep(2)
    cart_item_name = driver.find_element(By.CSS_SELECTOR, "p.product-name").text
    assert "Banana" in cart_item_name, "Item not found in cart!"

    print("Test Passed: Item successfully added to cart.")

    # Place order
    place_order_button = driver.find_element(By.XPATH, "//button[text()='Place Order']")
    place_order_button.click()

    # Select country
    time.sleep(2)
    country_dropdown = Select(driver.find_element(By.TAG_NAME, "select"))
    country_dropdown.select_by_visible_text("Cambodia")

    # Agree to terms and conditions
    time.sleep(2)
    agree_checkbox = driver.find_element(By.CSS_SELECTOR, "input.chkAgree")
    agree_checkbox.click()

    # Click on Proceed
    time.sleep(2)
    proceed_button = driver.find_element(By.XPATH, "//button[text()='Proceed']")
    proceed_button.click()

    print("Test Passed: Order successfully placed!")

finally:
    # Close the browser
    driver.quit()
