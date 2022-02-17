from selenium import webdriver


browser = webdriver.Chrome(executable_path='C:/chromedriver/chromedriver.exe')
browser.get("http://suninjuly.github.io/simple_form_find_task.html")
button = browser.find_element('id', "submit_button")
browser.quit()
