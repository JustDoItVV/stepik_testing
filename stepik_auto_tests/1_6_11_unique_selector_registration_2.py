from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link_1 = "http://suninjuly.github.io/registration1.html"
    link_2 = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link_2)

    input_1 = browser.find_element(By.XPATH, "//input[@placeholder='Input your first name']")
    input_1.send_keys('a')
    input_1 = browser.find_element(By.XPATH, "//input[@placeholder='Input your last name']")
    input_1.send_keys('b')
    input_1 = browser.find_element(By.XPATH, "//input[@placeholder='Input your email']")
    input_1.send_keys('c@c.c')

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    time.sleep(1)

    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()
