import time
from Auth import login
from product import choose_products
from Cart import view_cart
from payment import checkout

def main():
    # Credentials and data
    username = "standard_user"
    password = "secret_sauce"
    product_names = ["Sauce Labs Backpack", "Sauce Labs Bike Light", "Test.allTheThings() T-Shirt (Red)"]
    first_name = "John"
    last_name = "Doe"
    postal_code = "12345"

    # Login
    time.sleep(2)
    driver = login(username, password)

    # Choose products
    time.sleep(2)
    choose_products(driver, product_names)

    # View Cart
    time.sleep(2)
    view_cart(driver)

    # Checkout
    time.sleep(2)
    checkout(driver, first_name, last_name, postal_code)

    print("Test Completed!")
    driver.quit()

if __name__ == "__main__":
    main()
