from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time


# Initialize WebDriver
service = Service("/Users/lychandy/Documents/chromedriver")
driver = webdriver.Chrome(service=service)

try:
    # Open the URL
    driver.get("https://ultimateqa.com/filling-out-forms/")
    driver.maximize_window()

    # Wait for the page to load
    time.sleep(2)

    # first form

    name = driver.find_element(By.ID,"et_pb_contact_name_0")
    name.send_keys("tester")

    message = driver.find_element(By.NAME,"et_pb_contact_message_0")
    message.send_keys("boomer")

    #submit_btn = driver.find_element(By.NAME,"et_builder_submit_button")
    #submit_btn.click()
    time.sleep(2)

    print("form one : test passed !!")



    #second form
    name_one = driver.find_element(By.ID,"et_pb_contact_name_1")
    name_one.send_keys("tester one")

    message_one = driver.find_element(By.NAME,"et_pb_contact_message_1")
    message_one.send_keys("doooper")

    capcha = driver.find_element(By.XPATH,"//input[@name='et_pb_contact_captcha_1']")
    capcha.send_keys("20")

    submit_btn_one = driver.find_element(By.NAME,"et_builder_submit_button")
    submit_btn_one.click()


    time.sleep(2)
    print("form two : test passed !!")








finally:
    driver.quit()