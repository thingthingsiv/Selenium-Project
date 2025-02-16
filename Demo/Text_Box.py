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
    driver.get("https://demoqa.com/text-box")
    driver.maximize_window()

    # Wait for the page to load
    time.sleep(2)

    full_name = driver.find_element(By.ID, "userName")
    full_name.send_keys("sivthingthing")

    email = driver.find_element(By.ID,"userEmail")
    email.send_keys("testing@gmail.com")

    address = driver.find_element(By.CLASS_NAME,"form-control")
    address.send_keys("Phnom Penh")

    permanant_address = driver.find_element(By.ID,"permanentAddress")
    permanant_address.send_keys("Siem Reap")


    submit_btn = driver.find_element(By.CLASS_NAME,"btn btn-primary")
    submit_btn.click()

    time.sleep(2)
    print("test text box passed!!")





finally:
    driver.quit()