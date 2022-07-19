from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/execute_script.html")
    x_element = browser.find_element(By.ID, "input_value").text
    x = int(x_element)
    y = calc(x)
    #button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    #browser.execute_script("window.scrollBy(0, 200);")
    input = browser.find_element(By.ID, "answer")
    input.send_keys(y)
    check = browser.find_element(By.ID, "robotCheckbox")
    browser.execute_script("return arguments[0].scrollIntoView(true);", check)
    check.click()
    radio = browser.find_element(By.ID,"robotsRule")
    radio.click()
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()